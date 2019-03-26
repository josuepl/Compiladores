# -----------------------------------------------------------------------------
# yacc_simple.py
#
# A simple, properly specifier grammar
# -----------------------------------------------------------------------------
import sys

if ".." not in sys.path: sys.path.insert(0,"..")
import ply.yacc as yacc

from calclex import *

# Parsing rules
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }

def p_statement_assign(t):
    'statement : VAR EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    print("exp "+t[2]+"  "+ str(t[0]))


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_var(t):
    'expression : VAR'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_error(t):
    print("Syntax error at '%s'" % t.value)

def p_print(t):
    'statement : PRINT LPAREN expression RPAREN LIM'
    print("Funcion PRINT")
    print(t[3])
    
def p_statement_print_error(p):
    'statement : PRINT error'
    print("Syntax error in print statement. Bad expression")
    
#def p_expression_list(t):
    #'expression : expression, expression_list'
    

parser = yacc.yacc()
lexer = lex.lex()

while True:
    parser = yacc.yacc()
    lexer = lex.lex()
    try:
        data = input('calc > ')
        lexer.input(data)
    except EOFError:
            break
    if not data:   continue
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        print(tok)
    result = parser.parse(data)
    print("mensaje res"+str(result))
    print("mensaje toks"+str(tokens))
    





