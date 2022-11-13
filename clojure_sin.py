import ply.yacc as sintactico
from clojure_lex import tokens


def p_instrucciones(p): #puede probar imprimir(var)
  '''instrucciones : asignacion
                    | impresion
                    | sumatoria
                    | diferencia
                    | producto
                    | division
                    | condicional'''  
def p_asignacion(p): #puede reconocer a=20
  'asignacion : VARIABLE IGUAL valor'

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
def p_aritmetica1(p):
    '''operacion : MAS
          | MENOS
          | PRODUCTO
          | DIVISION
          | MENORQUE
          | MAYORQUE
          | MAYORIGUALQUE
          | MENORIGUALQUE
          | DIFERENTE
          | COMPARA_IGUAL'''

def p_suma(p):
    'sumatoria : LPAREN operacion valor valor RPAREN'

def p_resta(p):
    'diferencia : LPAREN operacion valor valor RPAREN'
    
def p_multiplicacion(p):
    'producto : LPAREN operacion valor valor RPAREN'
    
def p_division(p):
    'division : LPAREN operacion valor valor RPAREN'
    
def p_booleanos(p):
      'condicional : LPAREN operacion valor valor RPAREN'
      

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