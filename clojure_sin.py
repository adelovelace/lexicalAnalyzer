import ply.yacc as sintactico
from lexicalAnalyzer.clojure_lex import tokens
from bigtree import Node, shift_nodes, print_tree

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
  p[0] = ("INSTRUCCION", p[1])

def p_tipos_datos(p):
  '''dato : STRING
            | CHAR
            | ENTERO
            | FLOTANTE
            | BOOLEAN
            | VARIABLE '''
  p[0] = ('DATO', p[1])

def p_valor(p):
  '''valor : ENTERO
          | FLOTANTE
          | BOOLEAN
          '''
  p[0] = ('VALOR', p[1])

def p_operadoresComparadores(p):
    '''operador_comparadores : COMPARA_IGUAL
                | MENORQUE
                | MAYORQUE
                | MAYORIGUALQUE
                | MENORIGUALQUE
                | DIFERENTE'''
    p[0] = ('OP_COMPARADOR', p[1])

def p_asignacion(p): #puede reconocer (def x 10)
  '''asignacion : LPAREN DEFICION VARIABLE dato RPAREN
                | LPAREN LET LCOR VARIABLE dato RCOR RPAREN'''

  if len(p) == 6:
      p[0] = ('ASIGNACION', p[3], p[4])
  if len(p) == 8:
      p[0] = ('ASIGNACION', p[4], p[5])


def p_sentenciaBooleana(p):
    '''sentencia_booleana : LPAREN operador_comparadores dato dato RPAREN'''
    p[0] = ("SENTENCIA_BOOLEANA", p[2], p[3], p[4])

def p_linecondition(p):
    '''linecondition : sentencia_booleana impresion'''
    p[0] = ('DECLARACION', p[1])

#(cond (< 2 2) (println 1) (< 2 10) (println "1"))
#(cond (< 4 5) (println "3") (< 4 5) (println 3))
def p_cond(p):
    '''cond_ : LPAREN COND linecondition linecondition RPAREN'''
    p[0] = ("EXPRESION_COND", p[3], p[4])

#(cond (< 4 5) (println "3") (< 4 5) (println 3) : else (println 9))
def p_condElse(p):
    'cond_else : LPAREN COND linecondition linecondition DOSPUNTOS ELSE impresion RPAREN'
    p[0] = ("COND_ELSE", p[3], p[4], p[7])


# (case x 5 (println "x is 5") 10 (println "x is 10") (println "x is neither 5 nor 10"))
def p_case(p):
    '''case : dato impresion
            | dato dato STRING
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
def p_function(p):
    '''definition : LPAREN DEFFUNCION VARIABLE internos RPAREN
                | LPAREN DEFFUNCION internos if dato RPAREN
    '''


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
    #'if :  IF LPAREN operador_comparadores dato dato RPAREN'
    '''if : IF LPAREN operador_comparadores dato dato RPAREN
          | IF sentencia_booleana
          | IF sentencia_booleana recur
    '''
    #'if :  IF sentencia_booleana'


def p_if_do(p):
    'if_do : LPAREN IF LPAREN operador_comparadores dato dato RPAREN LPAREN DO LPAREN dato RPAREN BOOLEAN RPAREN RPAREN'

# def p_dotimes(p):
#     'dotimes: '

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
                        | LCOR dato vector_entero dato vector_entero RCOR
                        | LCOR vector_entero conjuntos RCOR

      '''

def p_doseq_prn(p):
      '''doseq_prn : PRN LPAREN dato RPAREN
                        | PRN LPAREN dato  dato RPAREN
                        | PRN LPAREN dato  dato dato RPAREN
      '''

def p_doseq(p):
      '''doseq : LPAREN DOSEQ doseq_args LPAREN impresion RPAREN RPAREN
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
      p[0] = ("", p[2], p[3])

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

def make_tree():
    root = Node("a", age=90)
    b = Node("b", age=65, parent=root)
    c = Node("c", age=60, parent=root)
    d = Node("d", age=40, parent=b)

    print_tree(root, attr_list=["age"])

def format_parser_tree(str_tree):
    output = ""
    tab_count = 0
    for l in str_tree:
        if l == '(':
            output +="\n"+"  "*tab_count +"("
            tab_count += 1
        elif l == ')':
            tab_count -= 1
            output += "  "*tab_count+")\n"
        else: output += l
    return output

def validaRegla(s):
    print(s)
    result = parser.parse(s)
    print(result)
    return format_parser_tree(str(result))


