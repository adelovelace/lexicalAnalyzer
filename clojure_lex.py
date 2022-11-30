import ply.lex as lex
from datetime import datetime

reserved = {
  'let': 'LET',
  'future': 'FUTURE',
  'def': 'DEFICION',
  'fn':'FUNCION',
  'class': 'CLASE',
  'println': 'IMPRIMIR',
  'new': 'NUEVO', 
  'if': 'IF',
  'do':'DO', 
  'when':'WHEN',
  'cond':'COND',
  'else': 'ELSE',
  'case':'CASE',
  'dotimes':'DOTIMES',
  'doseq':'DOSEQ',
  'loop':'LOOP',
  'recur':'RECURSION',
  'defn':'DEFFUNCION',
  'ns':'NS',
  'not':'NOT',
  'str':'STR',
  'recur':'RECUR',
  'inc':'INC',
  'increase':'INCREASE',
  'range' :'RANGE',
  'list': 'LIST',
  'prn' : 'PRN',
}

tokens = [
  'INPUT',
  'ENTERO',
  'FLOTANTE',
  'BOOLEAN',
  'CHAR',
  'STRING',
  'VECTOR',
  'MAPA',
  'CONJUNTOS',
  'MENOS',
  'MAS',
  'PRODUCTO',
  'DIVISION',
  'LPAREN',
  'RPAREN',
  'LCOR',
  'RCOR',
  'L_LLAVE',
  'R_LLAVE',
  'VARIABLE',
  'IGUAL',
  'MENORQUE',
  'MENORIGUALQUE',
  'MAYORQUE',
  'MAYORIGUALQUE',
  'DIFERENTE',
  'COMPARA_IGUAL',
  'LISTA',
  'NUMERAL',
  'DOSPUNTOS',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_MAS     = r'\+'
t_MENOS   = r'-'
t_PRODUCTO   = r'\*'
t_DIVISION = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LCOR = r'\['
t_RCOR = r'\]'
t_L_LLAVE = r'\{'
t_R_LLAVE = r'\}'
t_IGUAL = r'='
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_MAYORIGUALQUE = r'>='
t_MENORIGUALQUE = r'<='
t_DIFERENTE = r'!='
t_NUMERAL = r'\#'
t_DOSPUNTOS = r'\:'


# A regular expression rule with some action code
def t_FLOTANTE(t):
  #r'\d+\.\d+'
  r'\d+(\.\d+)'
  return t
  
def t_ENTERO(t):
  r'\d+' 
  return t

def t_BOOLEAN(t):
  r'(true|false)'
  t.type = reserved.get(t.value, 'BOOLEAN')
  return t

def t_VARIABLE(t):
  r'[a-zA-Z_][a-zA-Z0-9]*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t

# def t_VECTOR(t):
#     r'\[(\d+|\d+\s|\d+(\.\d+)?|\d+(\.\d+)?\s|\"[\w|\s|.|\S]*\"|\"[\w|\s|.|\S]*\"\s|true\s|\false\s|true|false)+\]'
#     return t

# def t_MAPA(t):
#     r'\{(\:\w+\-*\w+\s(\d+|\"[\w|\s|.|\S]*\")(\s|))+\}'
#     return t

def t_INPUT(t):
  r'\(read-line\)'
  return t

def t_LISTA(t):
  r'\(list\s([0-9]+\s*)+\)'
  return t

def t_CHAR(t):
  r'\\[a-zA-Z]{1}'
  return t

def t_STRING(t):
  r'\"([^\\\n]|(\\.))*?\"'
  #r'\"[\w|\s|.|\S]*\"'
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_COMMENTS(t):
  r'\;.*'
  pass

# Error handling rule
def t_error(t):
  print("Caracter no permitido'%s'" % t.value[0])
  t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


def getTokens(lexer):
  list_tokens = []
  for tok in lexer:
    list_tokens.append(tok)
    # print(tok)
  return list_tokens

def input_sentence(linea):
  lexer.input(linea)

  return getTokens(lexer)

#
# print(f'Seleccione el modo de prueba:\n1. Ingresar datos. \n2. Evaluar por defecto. (source.txt)\n')
# selector = input(">>")
# try:
#   selector = int(selector)
# except:
#   selector = -1
#
# if (selector == 1):
#
#   linea = " "
#   while linea != "":
#     linea = input("Ingrese >>")
#     lexer.input(linea)
#     getTokens(lexer)
#
# elif (selector == 2):
#
#   file = open('source.txt', 'r')
#   log_file = open('log.txt', 'a')
#   lines = file.readlines()
#   prueba = "Prueba: " + datetime.today().strftime("%d/%m/%Y") + " " + datetime.now().strftime("%H:%M:%S") + '\n'
#   for line in lines:
#     lexer.input(line)
#     getTokens(lexer)
#
#   log_file.writelines(prueba)
#
#   print("Archivo leido")
#
# else:
#   pass
#
# print("Succesfull")
