# Propositional Logic Parser

This Python script parses and evaluates propositional logic formulas using lexical analysis (tokenization) and parsing techniques. It supports the recognition of atomic propositions, logical connectives (negation, conjunction, disjunction, implication, equivalence), and parentheses for grouping.

## Installation

Ensure you have Python installed on your system. Additionally, install the required [PLY](https://github.com/dabeaz/ply) it's a zero-dependency Python implementation of the traditional parsing tools lex and yacc.

## Usage

1. Run the script using Python:
```python propositional_logic_parser.py```

2. Enter the propositional logic formula when prompted.
3. The script will tokenize the formula, parse it, and then evaluate whether the formula is satisfiable.

## Structure

- **/lib**: Contains the PLY libraries `yacc.py` and `lex.py`.

- **propositional_logic_parser.py**: The main file containing the parser implementation.

- **parser.out**: Generated file from PLY.

- **parsetab.py**: Generated file from PLY.


## Supported Tokens 

ATOM: A sequence of alphabetical characters representing atomic propositions.

NEGATION: '~' symbol for negation.

AND: '&' symbol for conjunction.

OR: '|' symbol for disjunction.

IMPLIES: '->' symbol for implication.

EQUIVALENT: '<->' symbol for equivalence.

LPAREN: '(' symbol for left parenthesis.

RPAREN: ')' symbol for right parenthesis.

## Example
Suppose you want to analyze the formula (A & B) | (~A & B). Upon running the script, you'll input this formula, and the script will determine whether it's satisfiable or not.

## Credits

This script utilizes the ply library for lexical analysis and parsing.
[PLY Documentation](https://www.dabeaz.com/ply/ply.html)

## Author

Michael DIOP ROGANDJI

Thierry LAGUERRE
