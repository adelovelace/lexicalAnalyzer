import ply.yacc as sintactico
from clojure_lex import tokens

def p_instrucciones(p): #puede probar imprimir(var)
  '''instrucciones : asignacion
                    | impresion
                    | operacion_aritmetica1
                    | condicional
                    | conjuntos
                    | vector
                    | mapa
                    | if
                    | do
                    | if_do
                    | when
                    | defn
                    | defn_with_return
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
# (case x 5 "x is 5" 10 "x is 10" :else "sdsd")
def p_case(p):
    '''case : dato impresion
            | dato STRING
    '''
def p_case_else(p):
      'case_else : DOSPUNTOS ELSE STRING'

def p_case_expression(p):
    '''case_expression : LPAREN CASE dato case case impresion RPAREN
            | LPAREN CASE dato case case case_else RPAREN
    '''

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

def p_increase(p):
      'increase : INCREASE LCOR dato RCOR'
      
def p_argumments(p):
    '''argumments : LCOR dato dato dato RCOR
                   | LCOR dato dato RCOR
                   | LCOR dato RCOR'''
def p_body(p):
    'body : instrucciones'
    
def p_recur(p):
      'recur : LPAREN RECUR LPAREN INC dato RPAREN RPAREN'
     

def p_internos(p):
    '''internos : description
                | argumments
                | body
                | increase
                | argumments body
                | description argumments body'''

#(defn holi "sp"[x] (println 2))
#(defn increase [i] (if (< i 10) (recur (inc i))i))
def p_function(p):
    '''definition : LPAREN DEFFUNCION VARIABLE internos RPAREN
                | LPAREN DEFFUNCION internos if dato RPAREN
    '''


def p_impresion(p):
  'impresion : LPAREN IMPRIMIR dato RPAREN'

def p_valor_variable(p):
  'valor : VARIABLE'

def p_vector(p):
  'vector : VECTOR'


def p_mapa(p):
  'mapa : MAPA'


def p_if(p):
    '''if : LPAREN IF instrucciones body RPAREN'''

def p_do(p):
    '''do : LPAREN DO instrucciones body RPAREN'''

def p_if_do(p):
    'if_do : LPAREN IF instrucciones body do RPAREN'

def p_when(p):
      '''when : LPAREN WHEN instrucciones body RPAREN'''

def p_dotimes(p):
    'dotimes: LPAREN DOTIMES instrucciones body RPAREN'

def p_op_aritmetica1(p):
    '''operacion : MAS
          | MENOS
          | PRODUCTO
          | DIVISION '''

#arrglar

def p_operacionesLogicas(p):
      """operacionesLogicas : LPAREN IF LPAREN MENORQUE VARIABLE ENTERO RPAREN LPAREN RECUR LPAREN INC LPAREN VARIABLE RPAREN RPAREN VARIABLE RPAREN RPAREN"""


def p_operacion_aritmetica1(p):
    'operacion_aritmetica1 : LPAREN operacion valor valor RPAREN'
    
def p_booleanos(p):
      'condicional : LPAREN operacion valor valor RPAREN'


#(doseq [n (range 3)](println n))
def p_doseq_args(p):
      '''doseq_args : LCOR dato LPAREN RANGE dato RPAREN RCOR
                        | LCOR dato conjuntos RCOR
                        | LCOR dato vector dato vector RCOR
                        | LCOR vector conjuntos RCOR
      
      '''

def p_doseq_prn(p):
      '''doseq_prn : PRN LPAREN dato RPAREN
                        | PRN dato dato
                        | PRN dato dato dato 
                        | PRN operacion_aritmetica1
      '''

# (doseq [a [1 2] b [3 4]] (println "a"))
# (doseq [a [1 2] b [3 4]] (prn (* x y)))
# (doseq [a [1 2] b [3 4]] (prn x y z))
# (doseq [a [1 2]] (prn x y))
# (doseq [[1 2] #{1 2 3}] (prn x y))
def p_doseq(p):
      '''doseq : LPAREN DOSEQ doseq_args impresion RPAREN
                        | LPAREN DOSEQ doseq_args LPAREN doseq_prn RPAREN RPAREN
      '''

def p_defn(p):
      '''defn : LPAREN DEFFUNCION VARIABLE LCOR VARIABLE RCOR LPAREN expresionDefnElse RPAREN RPAREN
                        | LPAREN DEFFUNCION INCREASE LCOR VARIABLE RCOR operacionesLogicas RPAREN
      
      '''  

def p_defn_with_return(p):
      '''defn_with_return : LPAREN DEFFUNCION VARIABLE LCOR VARIABLE RCOR LPAREN expresionDefnElse RPAREN RPAREN defn_return
                        | LPAREN DEFFUNCION INCREASE LCOR VARIABLE RCOR operacionesLogicas RPAREN defn_return
      
      ''' 

def p_expresionDefnElse(p):
      'expresionDefnElse : CASE VARIABLE expresionCase DOSPUNTOS ELSE STRING' 

  
def p_defn_return(p):
      'defn_return : LPAREN dato dato RPAREN'

def p_expresionCase(p):
      '''expresionCase : dato STRING '''
  
def p_conjuntos(p):
      '''conjuntos : NUMERAL L_LLAVE expresionConjuntoEnteros R_LLAVE
                      | NUMERAL L_LLAVE expresionConjuntoDouble R_LLAVE
                      | NUMERAL L_LLAVE expresionConjuntoString R_LLAVE
      '''


'''
def p_argumentsLoop(p):
      'argumentsLoop : dato dato'
                    
def p_recurLoop(p):
      'recurLoop : LPAREN RECURSION LPAREN INC dato RPAREN RPAREN'
'''

# (loop [i 0] (if (< i 10) (recur (inc i))i))
def p_sentenciaLoopRecur(p):
      'sentenciaLoopRecur : LPAREN LOOP argumments LPAREN if dato RPAREN RPAREN'

      
      
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