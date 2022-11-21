import ply.yacc as sintactico
from clojure_lex import tokens

def p_instrucciones(p): #puede probar imprimir(var)
  '''instrucciones : asignacion
                    | impresion
                    | operacion_aritmetica1
                    | condicional
                    | conjuntos
                    | vector_entero
                    | vector_flotante
                    | mapa_entero
                    | mapa_flotante
                    | if
                    | if_do
                    | defn
                    | operacionesLogicas
                    | sentenciaLoopRecur
                    | cond_
                    | cond_else
                    | doseq
                    | case_expression
                    | lista
                    | sentencia_booleana
                    | definition'''

def p_tipos_datos(p):
  '''dato : STRING
            | CHAR
            | ENTERO
            | FLOTANTE
            | BOOLEAN
            | VARIABLE '''
  
def p_valor(p):
  '''valor : ENTERO
          | FLOTANTE
          | BOOLEAN
          '''

def p_operadoresComparadores(p):
    '''operador_comparadores : COMPARA_IGUAL
                | MENORQUE
                | MAYORQUE
                | MAYORIGUALQUE
                | MENORIGUALQUE
                | DIFERENTE'''
  
def p_asignacion(p): #puede reconocer (def x 10)
  '''asignacion : LPAREN DEFICION VARIABLE dato RPAREN
                | LPAREN LET LCOR VARIABLE dato RCOR RPAREN'''

def p_sentenciaBooleana(p):
    '''sentencia_booleana : LPAREN operador_comparadores dato dato RPAREN'''

def p_linecondition(p):
    '''linecondition : sentencia_booleana impresion'''


#(cond (< 2 2) (println 1) (< 2 10) (println "1"))
#(cond (< 4 5) (println "3") (< 4 5) (println 3))

def p_cond(p):
    '''cond_ : LPAREN COND linecondition linecondition RPAREN'''

#(cond (< 4 5) (println "3") (< 4 5) (println 3) : else (println 9))
def p_condElse(p):
    'cond_else : LPAREN COND linecondition linecondition DOSPUNTOS ELSE impresion RPAREN'

# (case x 5 (println "x is 5") 10 (println "x is 10") (println "x is neither 5 nor 10"))
def p_case(p):
    'case : dato impresion'

def p_case_expression(p):
    'case_expression : LPAREN CASE dato case case impresion RPAREN'

#(list 2 "3")
def p_lista(p):
    'lista : LPAREN LIST dato dato RPAREN'

# (defn saludar
# 	“Retorna un saludo predeterminado con el nombre de la persona ingresada como parámetro”
# 	[ name ]
# 	( str “OH! Eres ” name “?! Que emoción verte nuevamente! :D” )
# )
def p_description(p):
    'description : STRING'

def p_argumments(p):
    '''argumments : LCOR dato dato dato RCOR
                   | LCOR dato dato RCOR
                   | LCOR dato RCOR'''
def p_body(p):
    'body : instrucciones'
def p_internos(p):
    '''internos : description
                | argumments
                | body
                | argumments body
                | description argumments body'''

#(defn holi "sp"[x] (println 2))
def p_function(p):
    'definition : LPAREN DEFFUNCION VARIABLE internos RPAREN'


def p_impresion(p):
  'impresion : LPAREN IMPRIMIR dato RPAREN'

def p_valor_variable(p):
  'valor : VARIABLE'


def p_vector_entero(p):
  'vector_entero : VECTOR_ENTERO'

def p_vector_flotante(p):
  'vector_flotante : VECTOR_FLOTANTE'

def p_mapa_entero(p):
  'mapa_entero : MAPA_ENTERO'

def p_mapa_flotante(p):
  'mapa_flotante : MAPA_FLOTANTE'

def p_if(p):
    'if :  IF LPAREN operador_comparadores dato dato RPAREN'

def p_if_do(p):
    'if_do : LPAREN IF LPAREN operador_comparadores dato dato RPAREN LPAREN DO LPAREN dato RPAREN BOOLEAN RPAREN RPAREN'

# def p_dotimes(p):
#     'dotimes: '

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