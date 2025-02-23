import itertools
from ply.lex import lex
from ply.yacc import yacc

# Token definition
tokens = ('ATOM','NEGATION','AND','OR','IMPLIES','EQUIVALENT','LPAREN','RPAREN')

# Regex Rules
t_ATOM = r'[a-zA-Z]+'
t_NEGATION = r'\~'
t_AND = r'\&'
t_OR = r'\|'
t_IMPLIES = r'\->'
t_EQUIVALENT = r'\<\-\>'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Ignore spaces and tabulations
t_ignore = ' \t'

# Check error with tokens
def t_error(t):
    print(f"Token not recognized : '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex()

# Input your formula
formula = str(input("Please enter a propositionnal formula :"))


lexer.input(formula)

print("---------------------")
print("Grammar tokens :")
while True :
    tok = lexer.token()
    if not tok :
        break
    print(tok)
print("---------------------")

# Grammar definition
def p_expr_atom(p):
    'expr : ATOM'
    p[0] = p[1]

def p_expr_parens(p):
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_expr_not(p):
    'expr : NEGATION expr'
    p[0] = ("NOT", p[2])

def p_expr_binop(p):
    '''expr : expr AND expr
            | expr OR expr
            | expr IMPLIES expr
            | expr EQUIVALENT expr'''
    p[0] = (p[2], p[1], p[3])


# Rule for managing syntax errors
def p_error(p):
    if p:
        print(f"Syntax error near '{p.value}' on line {p.lineno}")
        print("Make sure to use the symbol for operators : & , | ")
    else:
        print("Syntax error: unexpected end of file")
    exit()

# Creating the parser
parser = yacc()

# Evaluates the formula returns a boolean
def evaluate_formula(formula, variables):
    print(f"Evaluating formula: {formula}")  # Debugging-Ausgabe
    if isinstance(formula, str):  # if it's an atom
        return variables.get(formula, False)
    elif isinstance(formula, bool):  # if it's already evaluated
        return formula
    elif formula[0] == 'NOT':  # if it's a negation
        return not evaluate_formula(formula[1], variables)
    elif formula[0] == '&':  ## if it's AND  
        return evaluate_formula(formula[1], variables) and evaluate_formula(formula[2], variables)
    elif formula[0] == '|':  # # if it's OR 
        return evaluate_formula(formula[1], variables) or evaluate_formula(formula[2], variables)
    elif formula[0] == '->':  # if it's IMPLIES
        return evaluate_formula(formula[1], variables) or evaluate_formula(formula[2], variables)
    else:
        raise ValueError("Unrecognized formula")

# Lists all existing variables
def get_all_variables(formula):
    if isinstance(formula, str):  
        return {formula}
    elif isinstance(formula, bool):  
        return set()
    elif formula[0] == 'NOT':  
        return get_all_variables(formula[1])
    elif formula[0] == '&':  
        return get_all_variables(formula[1]).union(get_all_variables(formula[2]))
    elif formula[0] == '|':  
        return get_all_variables(formula[1]).union(get_all_variables(formula[2]))
    elif formula[0] == '->':  
        return get_all_variables(formula[1]).union(get_all_variables(formula[2]))
    else:
        raise ValueError("Formule non reconnue")


# Check the formula satisfiability 
def is_satisfiable(formula, variables):
    return evaluate_formula(formula, variables)

# Generate all combinaisons in the truth table
def generate_truth_assignments(variables):
    truth_values = [True, False]
    truth_assignments = itertools.product(truth_values, repeat=len(variables))
    return [{variables[i]: assignment[i] for i in range(len(variables))} for assignment in truth_assignments]

# Check for all combinaisons in the truth table if the formula is satisfiable
def is_satisfiable_for_all_assignments(formula, variables):
    truth_assignments = generate_truth_assignments(variables)
    for assignment in truth_assignments:
        if is_satisfiable(formula, assignment):
            print("Example of satisfiability with the values : ",assignment)
            return True
    return False

# Parse the propositional formula
def parse_propositional_formula(formula):
    return parser.parse(formula)

# Main 
if __name__ == "__main__":
    # EX 1 
    parsed_formula = parse_propositional_formula(formula)
    print(f"Parsed formula: {parsed_formula}")  # Debugging-Ausgabe
    variables = get_all_variables(parsed_formula)
    print("Recognized formula", parsed_formula)
    # EX 2 
    print("Variable in the truth table", variables)
    if is_satisfiable_for_all_assignments(parsed_formula, list(variables)):
        print("The formula is satisfiable")
    else:
        print("The formula is unsatisfiable")
