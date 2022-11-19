import ply.yacc as sintactico
from clojure_lex import tokens

def p_instrucciones(p): #puede probar imprimir(var)
  '''instrucciones : asignacion
                    | impresion
                    | operacion_aritmetica1
                    | condicional
                    | vectores
                    | conjuntos
                    | defn
                    | operacionesLogicas
                    | sentenciaLoopRecur
                    | doseq'''

def p_tipos_datos(p):
  '''dato : STRING 
          | CHAR
          | ENTERO
          | FLOTANTE
          | BOOLEAN
          '''
  
def p_valor(p):
  '''valor : ENTERO
          | FLOTANTE
          | BOOLEAN
          '''
  
def p_asignacion(p): #puede reconocer (def x 10)
  '''asignacion : LPAREN DEFICION VARIABLE dato RPAREN '''

def p_impresion(p):
  'impresion : IMPRIMIR LPAREN valor RPAREN'

def p_valor_variable(p):
  'valor : VARIABLE'

# suma
def p_op_aritmetica1(p):
    '''operacion : MAS
          | MENOS
          | PRODUCTO
          | DIVISION '''

def p_operacionesLogicas(p):
      """operacionesLogicas : LPAREN IF LPAREN MENORQUE VARIABLE ENTERO RPAREN LPAREN RECUR LPAREN INC LPAREN VARIABLE RPAREN RPAREN VARIABLE RPAREN RPAREN"""

def p_operacion_aritmetica1(p):
    'operacion_aritmetica1 : LPAREN operacion valor valor RPAREN'
    
def p_booleanos(p):
      'condicional : LPAREN operacion valor valor RPAREN'
      
def p_vectores(p):
      'vectores : VECTORES'

def p_doseq(p):
      'doseq : LPAREN DOSEQ LCOR VARIABLE LPAREN RANGE VARIABLE RPAREN RCOR LPAREN impresion RPAREN RPAREN'      

def p_defn(p):
      '''defn : LPAREN DEFFUNCION VARIABLE LCOR VARIABLE RCOR LPAREN expresionDefnElse RPAREN RPAREN
                        | LPAREN DEFFUNCION INCREASE LCOR VARIABLE RCOR operacionesLogicas RPAREN
      
      '''  

def p_expresionDefnElse(p):
      'expresionDefnElse : CASE VARIABLE expresionCase DOSPUNTOS ELSE STRING' 

  
def p_expresionCase(p):
      '''expresionCase : dato STRING '''
  
def p_conjuntos(p):
      '''conjuntos : NUMERAL L_LLAVE expresionConjuntoEnteros R_LLAVE
                      | NUMERAL L_LLAVE expresionConjuntoDouble R_LLAVE
                      | NUMERAL L_LLAVE expresionConjuntoString R_LLAVE
      
      '''
      
def p_sentenciaLoopRecur(p):
      'sentenciaLoopRecur : LPAREN LOOP LCOR VARIABLE ENTERO RCOR  operacionesLogicas RPAREN'
      
def p_expresionConjuntoEnteros(p):
      '''expresionConjuntoEnteros : ENTERO
                     | ENTERO expresionConjuntoEnteros
    '''

def p_expresionConjuntoDouble(p):
      '''expresionConjuntoDouble : FLOTANTE
                     | FLOTANTE expresionConjuntoDouble
    '''

def p_expresionConjuntoString(p):
      '''expresionConjuntoString : STRING
                     | STRING expresionConjuntoString
    '''  

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