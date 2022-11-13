import ply.lex as lex


reserved = {
  'let': 'LET',
  'future': 'FUTURE',
  'def': 'DEFICION',
  'fn':'FUNCION',
  'defmacro': 'DEFMACRO',
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
}

tokens = [
  'ENTERO',
  'FLOTANTE',
  'BOOLEAN',
  'VECTORES',
  'CONJUNTOS',
  'MAPAS',
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
  'PUNTO_COMA',
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
t_MENORIGUALQUE = r'>='
t_DIFERENTE = r'!='
t_COMPARA_IGUAL = r'=='
t_PUNTO_COMA = r';'

# A regular expression rule with some action code
def t_FLOTANTE(t):
  r'\d+\.\d+'
  return t
  
def t_ENTERO(t):
  r'\d+' 
  return t

def t_VARIABLE(t):
  r'[a-zA-Z_][a-zA-Z0-9]*'
  t.type = reserved.get(t.value,'VARIABLE')
  return t

def t_BOOLEAN(t):
    r'(true|false)'
    t.type = reserved.get(t.value,'BOOLEAN')
    return t
  
def t_VECTORES(t):
      r'^[\[]([a-zA-Z0-9]+[\s][a-zA-Z0-9]+)+[\]]$'
      t.type = reserved.get(t.value,'VECTORES')
      return t
    
def t_CONJUNTOS(t):
      r'^\#[\{]{1}(([a-zA-Z]+[\s]{0,})+|([\d]+[\s]{0,})+){1,}[\}]{1}'
      t.type = reserved.get(t.value,'CONJUNTOS')
      return t

def t_MAPAS(t):
      r'^[\{](([\:]{1}[\w]+[\s][\w]+)[\s]{0,})+[\}]$'
      t.type = reserved.get(t.value,'MAPAS')
      return t
  
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_COMMENTS(t):
  r'\#.*'
  pass
  
# Error handling rule
def t_error(t):
  print("Caracter no permitido'%s'" % t.value[0])
  t.lexer.skip(1)
 
 # Build the lexer
lexer = lex.lex()

