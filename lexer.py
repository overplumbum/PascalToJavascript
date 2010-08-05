# ----------------------------------------------------------------------
# paslex.py
#
# A lexer for Pascal
# ----------------------------------------------------------------------

import sys
import ply.lex as lex

# Reserved words
reserved = (
    'AND', 'ARRAY', 'CASE', 'CONST', 'DIV', 'DO', 'DOWNTO', 'ELSE', 'END', 'FOR', 'FORWARD', 'FUNCTION', 'GOTO', 'IF', 'IN', 'LABEL', 'MOD', 
    'NIL', 'NOT', 'OF', 'OR', 'OTHERWISE', 'PACKED', 'PROCEDURE', 
    'RECORD', 'REPEAT', 'SET', 'THEN', 'TO', 'TYPE', 'UNTIL', 'VAR', 
    'WHILE', 'WITH', 
    'SHL', 'SHR',
    'EXTERNAL',
    #'PROGRAM', 
    )
reserved = dict(zip(map(str.lower, reserved), reserved))
reserved.update({
    'begin': 'PBEGIN',
    'file': 'PFILE',
})
#import pprint
#pprint.pprint(reserved)
    
tokens = tuple(reserved.values()) + (
    'IDENTIFIER',
    'CHARACTER_STRING', 
    #'REALNUMBER', 
    'ASSIGNMENT', 'COLON', 'COMMA', 'DIGSEQ', 
    'DOT', 'DOTDOT', 'EQUAL', 'GE', 'GT', 'LBRAC', 'LE', 'LPAREN', 
    'LT', 'MINUS', 'NOTEQUAL', 'PLUS', 'RBRAC',  
    'RPAREN', 'SEMICOLON', 'SLASH', 'STAR', 'STARSTAR', 'UPARROW', 
    )
    
# Completely ignored characters
t_ignore           = ' \t\x0c\r'

# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

t_ASSIGNMENT = r':='
t_COLON = r':'
t_COMMA = r','
t_DIGSEQ = r'[0-9]+'
#r_REALNUMBER = r'[0-9]+[.][0-9]+'
t_DOT = r'\.'
t_DOTDOT = r'\.\.'
t_EQUAL = r'='
t_GE = r'>='
t_GT = r'>'
t_LBRAC = r'\['
t_LE = r'<='
t_LPAREN = r'\('
t_LT = r'<'
t_MINUS = r'-'
t_NOTEQUAL = r'<>'
t_PLUS = r'\+'
t_RBRAC = r'\]'
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_SLASH = r'/(?=[^/])'
t_STAR = r'\*'
t_STARSTAR = r'\*\*'
t_UPARROW = r'\^|->'
t_CHARACTER_STRING = r"'([^']|\'\')*?'"

# Identifiers and reserved words

def t_IDENTIFIER(t):
    r'[a-zA-Z\_]([a-zA-Z0-9\_])*'
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t

def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)

# Comments
def t_comment(t):
    r'//.*'
    #r'(/\*(.|\n)*?*/)|(//.*)'
    t.lexer.lineno += 1



    
lexer = lex.lex(optimize=1)
if __name__ == "__main__":
    lex.runmain(lexer)

