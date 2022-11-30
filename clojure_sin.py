import ply.yacc as sintactico
from lexicalAnalyzer.clojure_lex import tokens

global error_info
error_info = ""


def p_instrucciones(p):  # puede probar imprimir(var)
    '''instrucciones : asignacion
                    | impresion
                    | operacion_aritmetica
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
                    | function
                    | dotimes
                    | ciclo
                    | valor'''
    p[0] = ("INSTRUCCION", p[1])


def p_tipos_datos(p):
    '''dato : STRING
            | CHAR
            | ENTERO
            | FLOTANTE
            | BOOLEAN
            | VARIABLE '''
    p[0] = ("DATO", p[1])


def p_valor(p):
    '''valor : ENTERO
          | FLOTANTE
          | BOOLEAN
          '''
    p[0] = ("VALOR", p[1])


def p_operadoresComparadores(p):  # BOLEANOS
    '''operador_comparadores : COMPARA_IGUAL
                | MENORQUE
                | MAYORQUE
                | MAYORIGUALQUE
                | MENORIGUALQUE
                | DIFERENTE'''
    p[0] = ('OP_COMPARADOR', p[1])


def p_op_aritmetica1(p):  # OP. MATEMICAS
    '''operador_aritmetico : MAS
                  | MENOS
                  | PRODUCTO
                  | DIVISION '''
    p[0] = ("OPERADOR_ARITMETICO", p[1])


def p_asignacion(p):  # puede reconocer (def x 10)
    '''asignacion : LPAREN DEFICION VARIABLE dato RPAREN
                | LPAREN LET LCOR VARIABLE dato RCOR RPAREN'''

    if len(p) == 6:
        p[0] = ('ASIGNACION', p[3], p[4])
    if len(p) == 8:
        p[0] = ('ASIGNACION', p[4], p[5])


# (< 2 2)
def p_sentenciaBooleana(p):
    '''sentencia_booleana : LPAREN operador_comparadores dato dato RPAREN'''
    p[0] = ("SENTENCIA_BOOLEANA", p[2], p[3], p[4])


# (< 2 2) (println "1")
def p_linecondition(p):
    '''linecondition : sentencia_booleana impresion'''
    p[0] = ("SENTENCIA", p[1], p[2])


# (cond (< 2 2) (println 1) (< 2 10) (println "1"))
# (cond (< 4 5) (println "3") (< 4 5) (println 3))
def p_cond(p):
    '''cond_ : LPAREN COND linecondition linecondition RPAREN'''
    p[0] = ("EXPRESION_COND", p[3], p[4])


# (cond (< 4 5) (println "3") (< 4 5) (println 3) : else (println 9))
def p_condElse(p):
    'cond_else : LPAREN COND linecondition linecondition DOSPUNTOS ELSE impresion RPAREN'
    p[0] = ("COND_ELSE", p[3], p[4], p[7])


# (case x
#   5
#       (println "x is 5")
#   10
#       (println "x is 10")
#   (println "x is neither 5 nor 10"))
# (case x 5 "x is 5" 10 "x is 10" :else "sdsd")
def p_case(p):
    '''case : dato impresion
            | dato STRING
            | dato impresion case
            | dato STRING case
    '''

    if len(p) == 3:
        p[0] = (p[1], p[2])
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])


def p_case_expression(p):
    '''case_expression : LPAREN CASE dato case impresion RPAREN
                        | LPAREN CASE dato case DOSPUNTOS ELSE STRING RPAREN
    '''

    if len(p) == 7:
        p[0] = ("CASE_EXPRESSION", p[3], p[5])
    if len(p) == 9:
        p[0] = ("CASE_EXPRESSION", p[3], p[7])


def p_argumentos_lista(p):
    '''argumentos_lista : dato
                        | dato argumentos_lista'''
    if len(p) == 2:
        p[0] = ("ARGUMENTO", p[1])
    if len(p) == 3:
        p[0] = ("ARGUMENTO", p[1], p[2])


# (list 2 "3")
def p_lista(p):
    'lista : LPAREN LIST argumentos_lista RPAREN'
    p[0] = ("LISTA", p[3])


# (defn saludar
# 	“Retorna un saludo predeterminado con el nombre de la persona ingresada como parámetro”
# 	[ name ]
# 	( str “OH! Eres ” name “?! Que emoción verte nuevamente! :D” )
# )
def p_description(p):
    'description : STRING'
    p[0] = ("DESCRIPCION", p[1])


def p_increase(p):
    'increase : INCREASE LCOR dato RCOR'
    p[0] = ("INCREASE", p[3])


def p_argumments(p):
    'argumments : LCOR argumentos_lista RCOR'
    p[0] = ("ARGUMENTOS", p[2])


def p_body(p):
    'body : instrucciones'
    p[0] = ("BODY", p[1])


def p_recur(p):
    'recur : LPAREN RECUR LPAREN INC dato RPAREN RPAREN'
    p[0] = ("RECUR", p[5])


def p_internos(p):
    '''internos : description
                | argumments
                | body
                | increase
                | argumments body
                | description argumments body'''

    if len(p) == 2:
        p[0] = (p[1])
    if len(p) == 3:
        p[0] = (p[1], p[2])
    if len(p) == 4:
        p[0] = (p[1], p[2], p[3])


# (defn holi "sp"[x] (println 2))
# (defn increase [i] (if (< i 10) (recur (inc i))i))
def p_function(p):
    '''function : LPAREN DEFFUNCION VARIABLE internos RPAREN
                | LPAREN DEFFUNCION internos if dato RPAREN
    '''
    if len(p) == 6:
        p[0] = ("FUNCION", p[3], p[4])
    if len(p) == 7:
        p[0] = ("FUNCION", p[3], p[4], p[5])


def p_impresion(p):
    'impresion : LPAREN IMPRIMIR dato RPAREN'

    p[0] = ("IMPRESION", p[3])


# [1 2 3 4]
# [true 3 "four" 5]
def p_secuencia_vector(p):
    ''' secuencia_v : dato 
                    | dato secuencia_v
    '''
    if len(p) == 2:
        p[0] = ("SECUENCIA DE VECTOR", p[1])
    if len(p) == 3:
        p[0] = ("SECUENCIA DE VECTOR", p[2])


def p_vector(p):
    'vector : LCOR secuencia_v RCOR'
    p[0] = ("VECTOR", p[2])


# Andrea (mapa y vector)

# {:page-count 362 :title "Oliver Twist" :author "Dickens" :published 1838}
def p_secuencia_mapa(p):
    ''' secuencia_mapa : DOSPUNTOS VARIABLE dato 
        | DOSPUNTOS VARIABLE secuencia_mapa
    '''
    p[0] = ("SECUENCIA DE MAPA", p[2], p[3])


def p_mapa(p):
    'mapa : L_LLAVE secuencia_mapa R_LLAVE'
    p[0] = ("MAPA", p[2])


def p_if(p):
    '''if : IF sentencia_booleana
          | IF sentencia_booleana recur
          | LPAREN IF instrucciones body RPAREN
    '''

    if len(p) == 3:
        p[0] = ("IF", p[2])
    if len(p) == 4:
        p[0] = ("IF", p[2], p[3])
    if len(p) == 5:
        p[0] = ("IF", p[3], p[4])


def p_do(p):
    '''do : LPAREN DO instrucciones RPAREN'''
    p[0] = ("DO", p[3])


def p_if_do(p):
    'if_do : LPAREN if do RPAREN'
    p[0] = ("IF_DO", p[2], p[3])


def p_when(p):
    '''when : LPAREN WHEN sentencia_booleana body RPAREN'''
    p[0] = ("WHEN", p[3], p[4])


def p_ciclo(p):
    'ciclo : LCOR VARIABLE ENTERO RCOR'
    p[0] = (p[2], p[3])


def p_dotimes(p):
    'dotimes : LPAREN DOTIMES ciclo body RPAREN'
    p[0] = ("DOTIMES", p[3], p[4])


def p_operacionesLogicas(p):
    '''operacionesLogicas : LPAREN if recur VARIABLE RPAREN RPAREN'''
    p[0] = (p[2], p[3], p[4])


def p_operacion_aritmetica1(p):
    'operacion_aritmetica : LPAREN operador_aritmetico dato dato RPAREN'
    p[0] = ("OP_ARITMETICA", p[2], p[4])


# (doseq [n (range 3)](println n))
def p_doseq_args(p):
    '''doseq_args : LCOR dato LPAREN RANGE dato RPAREN RCOR
                    | LCOR dato conjuntos RCOR
                    | LCOR dato vector dato vector RCOR
                    | LCOR vector conjuntos RCOR'''

    if p[4] == 'range':
        p[0] = ("DOSEQ_ARGS", p[2], p[5])
    if len(p) == 5:
        p[0] = ("DOSEQ_ARGS", p[2], p[3])
    if len(p) == 7:
        p[0] = ("DOSEQ_ARGS", p[2], p[3], p[4], p[5])


def p_doseq_prn(p):
    '''doseq_prn : PRN LPAREN dato RPAREN
                    | PRN dato dato
                    | PRN dato dato dato
                    | PRN operacion_aritmetica
      '''
    if len(p) == 5:
        p[0] = ("DOSEQ_PRN", p[3])
    if len(p) == 4:
        p[0] = ("DOSEQ_PRN", p[3])
    if len(p) == 5:
        p[0] = ("DOSEQ_PRN", p[3])
    if len(p) == 5:
        p[0] = ("DOSEQ_PRN", p[3])


# (doseq [a [1 2] b [3 4]] (println "a"))
# (doseq [a [1 2] b [3 4]] (prn (* x y)))
# (doseq [a [1 2] b [3 4]] (prn x y z))
# (doseq [a [1 2]] (prn x y))
# (doseq [[1 2] #{1 2 3}] (prn x y))
def p_doseq(p):
    '''doseq : LPAREN DOSEQ doseq_args impresion RPAREN
            | LPAREN DOSEQ doseq_args LPAREN doseq_prn RPAREN RPAREN
    '''
    if len(p) == 6:
        p[0] = ("DOSEQ", p[3], p[4])
    if len(p) == 8:
        p[0] = ("DOSEQ", p[3], p[5])


def p_defn(p):
    '''defn : LPAREN DEFFUNCION VARIABLE LCOR VARIABLE RCOR LPAREN expresionDefnElse RPAREN RPAREN
             | LPAREN DEFFUNCION INCREASE LCOR VARIABLE RCOR operacionesLogicas RPAREN
    '''
    if len(p) == 8:
        p[0] = ("DEFN", p[3], p[5], p[8])
    if len(p) == 9:
        p[0] = ("DEFN", p[3], p[5], p[7])


def p_defn_with_return(p):
    '''defn_with_return : LPAREN DEFFUNCION VARIABLE LCOR VARIABLE RCOR LPAREN expresionDefnElse RPAREN RPAREN defn_return
                        | LPAREN DEFFUNCION INCREASE LCOR VARIABLE RCOR operacionesLogicas RPAREN defn_return

      '''
    if len(p) == 12:
        p[0] = ("Defn_Return", p[3], p[5], p[8], p[11])
    if len(p) == 10:
        p[0] = ("Defn_Return", p[3], p[5], p[7], p[9])


def p_expresionDefnElse(p):
    'expresionDefnElse : CASE VARIABLE expresionCase DOSPUNTOS ELSE STRING'
    p[0] = ("ExpresionDefnElse", p[2], p[3], p[6])


def p_defn_return(p):
    'defn_return : LPAREN dato dato RPAREN'
    p[0] = ("DEFN_RETURN", p[2], p[3])


def p_expresionCase(p):
    '''expresionCase : dato STRING'''
    p[0] = (p[1], p[2])


# #{2 4 5 6}
def p_conjuntos(p):
    '''conjuntos : NUMERAL L_LLAVE expresionConjuntoEnteros R_LLAVE
                      | NUMERAL L_LLAVE expresionConjuntoDouble R_LLAVE
                      | NUMERAL L_LLAVE expresionConjuntoString R_LLAVE
      '''
    p[0] = ("CONJUNTOS", p[1], p[3])


# (loop [i 0] (if (< i 10) (recur (inc i))i))
def p_sentenciaLoopRecur(p):
    'sentenciaLoopRecur : LPAREN LOOP argumments LPAREN if dato RPAREN RPAREN'

    p[0] = ("SENTENCIA_LOOP", p[3], p[5], p[6])


def p_expresionConjuntoEnteros(p):
    '''expresionConjuntoEnteros : ENTERO
                                 | ENTERO expresionConjuntoEnteros
    '''

    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 3:
        p[0] = (p[1], p[2])


def p_expresionConjuntoDouble(p):
    '''expresionConjuntoDouble : FLOTANTE
                     | FLOTANTE expresionConjuntoDouble
    '''
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 3:
        p[0] = (p[1], p[2])


def p_expresionConjuntoString(p):
    '''expresionConjuntoString : STRING
                                  | STRING expresionConjuntoString
    '''
    if len(p) == 2:
        p[0] = p[1]
    if len(p) == 3:
        p[0] = (p[1], p[2])


# Error rule for syntax errors
def p_error(p):
    if p:
        print(f"Error de sintaxis - Token: {p.type}, Línea: {p.lineno}, Col: {p.lexpos}")
        parser.errok()
    else:
        print("Error de sintaxis Fin de Linea")


# Build the parser
parser = sintactico.yacc()


def format_parser_tree(str_tree):
    output = ""
    tab_count = 0
    for l in str_tree:
        if l == '(':
            output += "\n" + "  " * tab_count + "("
            tab_count += 1
        elif l == ')':
            tab_count -= 1
            output += "  " * tab_count + ")\n"
        else:
            output += l
    return output


def validaRegla(s):
    # print(f"s -> {s}")
    result = parser.parse(s)
    print(f"result-> {result}")

    return format_parser_tree(str(result))
