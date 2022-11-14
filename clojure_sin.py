import ply.yacc as sintactico
from clojure_lex import tokens


def p_instrucciones(p): #puede probar imprimir(var)
  '''instrucciones : asignacion
                    | impresion
                    | operacion_aritmetica1
                    | condicional
                    | vectores
                    | conjuntos
                    | mapas'''
                      
def p_asignacion(p): #puede reconocer a=20
  'asignacion : LPAREN DEFICION VARIABLE valor R_LLAVE'

def p_impresion(p):
  'impresion : IMPRIMIR LPAREN valor RPAREN'

def p_valor(p):
  '''valor : ENTERO
          | FLOTANTE
          | BOOLEAN
          '''
def p_valor_variable(p):
  'valor : VARIABLE'

# suma
def p_op_aritmetica1(p):
    '''operacion : MAS
          | MENOS
          | PRODUCTO
          | DIVISION '''

def p_operacion_aritmetica1(p):
    'operacion_aritmetica1 : LPAREN operacion valor valor RPAREN'
    
def p_booleanos(p):
      'condicional : LPAREN operacion valor valor RPAREN'
      
def p_vectores(p):
      'vectores : VECTORES'
      
def p_conjuntos(p):
      'conjuntos : CONJUNTOS'
    
def p_mapas(p):
      'mapas : MAPAS'
      
 # Error rule for syntax errors
def p_error(p):
  if p:
    print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
    parser.errok()
  else:
    print("Error de sintaxis Fin de Linea")
 
 # Build the parser
parser = sintactico.yacc()

def validaRegla(s):
  result = parser.parse(s)
  print(result)
