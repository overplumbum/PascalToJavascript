# %{
# /*
#  * grammar.y
#  *
#  * Pascal grammar in Yacc format, based originally on BNF given
#  * in "Standard Pascal -- User Reference Manual", by Doug Cooper.
#  * This in turn is the BNF given by the ANSI and ISO Pascal standards,
#  * and so, is PUBLIC DOMAIN. The grammar is for ISO Level 0 Pascal.
#  * The grammar has been massaged somewhat to make it LALR, and added
#  * the following extensions.
#  *
#  * constant expressions
#  * otherwise statement in a case
#  * productions to correctly match else's with if's
#  * beginnings of a separate compilation facility
#  */
# 
# %}

import sys
import ply.yacc as yacc
from lexer import tokens, lexer
import re

precedence =  []
start="script"

def p_script(t):
    'script : block DOT'
    t[0] = t[1]

# -------------- RULES ----------------
from parser_rules import *

def p_error(t):
    print("Error:", t)

from ply import *

def render(content, debug = False):
    parser = yacc.yacc()
    return parser.parse(content, lexer=lexer, debug = debug)

if __name__ == '__main__':
    if len(sys.argv)>1:
        print render(open(sys.argv[1]).read(), True)
