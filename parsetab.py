
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOLEAN CASE CHAR CLASE COMPARA_IGUAL COND CONJUNTOS DEFFUNCION DEFICION DIFERENTE DIVISION DO DOSEQ DOSPUNTOS DOTIMES ELSE ENTERO FLOTANTE FUNCION FUTURE IF IGUAL IMPRIMIR INC INCREASE INPUT LCOR LET LISTA LOOP LPAREN L_LLAVE MAPAS MAS MAYORIGUALQUE MAYORQUE MENORIGUALQUE MENORQUE MENOS NOT NS NUEVO NUMERAL PRODUCTO RANGE RCOR RECUR RPAREN R_LLAVE STR STRING VARIABLE VECTORES WHENinstrucciones : asignacion\n                    | impresion\n                    | operacion_aritmetica1\n                    | condicional\n                    | vectores\n                    | conjuntos\n                    | defn\n                    | operacionesLogicas\n                    | sentenciaLoopRecur\n                    | doseq\n                    | cond_\n                    | sentencia_booleana\n                    | operador_comparadoresdato : STRING\n            | CHAR\n            | ENTERO\n            | FLOTANTE\n            | BOOLEANvalor : ENTERO\n          | FLOTANTE\n          | BOOLEAN\n          operador_comparadores : COMPARA_IGUAL\n                | MENORQUE\n                | MAYORQUE\n                | MAYORIGUALQUE\n                | MENORIGUALQUE\n                | DIFERENTEasignacion : LPAREN DEFICION VARIABLE dato RPAREN\n                | LPAREN LET LCOR VARIABLE dato RCOR RPARENsentencia_booleana : LPAREN operador_comparadores dato dato RPARENlinecondition : sentencia_booleana impresion\n                    | sentencia_booleana datocond_ : LPAREN COND linecondition RPARENimpresion : LPAREN IMPRIMIR dato RPARENvalor : VARIABLEoperacion : MAS\n          | MENOS\n          | PRODUCTO\n          | DIVISION operacionesLogicas : LPAREN IF LPAREN MENORQUE VARIABLE ENTERO RPAREN LPAREN RECUR LPAREN INC LPAREN VARIABLE RPAREN RPAREN VARIABLE RPAREN RPARENoperacion_aritmetica1 : LPAREN operacion valor valor RPARENcondicional : LPAREN operacion valor valor RPARENvectores : VECTORESdoseq : LPAREN DOSEQ LCOR VARIABLE LPAREN RANGE VARIABLE RPAREN RCOR LPAREN impresion RPAREN RPARENdefn : LPAREN DEFFUNCION VARIABLE LCOR VARIABLE RCOR LPAREN expresionDefnElse RPAREN RPAREN\n                        | LPAREN DEFFUNCION INCREASE LCOR VARIABLE RCOR operacionesLogicas RPAREN\n      \n      expresionDefnElse : CASE VARIABLE expresionCase DOSPUNTOS ELSE STRINGexpresionCase : dato STRING conjuntos : NUMERAL L_LLAVE expresionConjuntoEnteros R_LLAVE\n                      | NUMERAL L_LLAVE expresionConjuntoDouble R_LLAVE\n                      | NUMERAL L_LLAVE expresionConjuntoString R_LLAVE\n      sentenciaLoopRecur : LPAREN LOOP LCOR VARIABLE ENTERO RCOR  operacionesLogicas RPARENexpresionConjuntoEnteros : ENTERO\n                     | ENTERO expresionConjuntoEnteros\n    expresionConjuntoDouble : FLOTANTE\n                     | FLOTANTE expresionConjuntoDouble\n    expresionConjuntoString : STRING\n                     | STRING expresionConjuntoString\n    '
    
_lr_action_items = {'LPAREN':([0,29,32,59,75,95,97,98,100,106,117,118,123,126,],[15,54,57,79,94,-30,103,104,104,112,122,123,79,129,]),'VECTORES':([0,],[16,]),'NUMERAL':([0,],[17,]),'COMPARA_IGUAL':([0,15,57,],[19,19,19,]),'MENORQUE':([0,15,54,57,],[18,18,73,18,]),'MAYORQUE':([0,15,57,],[20,20,20,]),'MAYORIGUALQUE':([0,15,57,],[21,21,21,]),'MENORIGUALQUE':([0,15,57,],[22,22,22,]),'DIFERENTE':([0,15,57,],[23,23,23,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,18,19,20,21,22,23,69,76,81,82,83,87,89,95,102,111,113,119,133,138,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-43,-23,-22,-24,-25,-26,-27,-34,-33,-49,-50,-51,-28,-41,-30,-29,-46,-52,-45,-44,-40,]),'DEFICION':([15,],[24,]),'LET':([15,],[25,]),'IMPRIMIR':([15,79,],[26,26,]),'DEFFUNCION':([15,],[28,]),'IF':([15,104,],[29,29,]),'LOOP':([15,],[30,]),'DOSEQ':([15,],[31,]),'COND':([15,],[32,]),'MAS':([15,],[34,]),'MENOS':([15,],[35,]),'PRODUCTO':([15,],[36,]),'DIVISION':([15,],[37,]),'L_LLAVE':([17,],[38,]),'STRING':([18,19,20,21,22,23,26,33,38,39,42,43,44,45,46,59,60,66,68,95,116,121,128,],[-23,-22,-24,-25,-26,-27,42,42,66,42,-14,-15,-16,-17,-18,42,42,66,42,-30,42,125,131,]),'CHAR':([18,19,20,21,22,23,26,33,39,42,43,44,45,46,59,60,68,95,116,],[-23,-22,-24,-25,-26,-27,43,43,43,-14,-15,-16,-17,-18,43,43,43,-30,43,]),'ENTERO':([18,19,20,21,22,23,26,27,33,34,35,36,37,38,39,42,43,44,45,46,47,48,49,50,51,59,60,64,68,74,92,95,116,],[-23,-22,-24,-25,-26,-27,44,48,44,-36,-37,-38,-39,64,44,-14,-15,-16,-17,-18,48,-19,-20,-21,-35,44,44,64,44,93,99,-30,44,]),'FLOTANTE':([18,19,20,21,22,23,26,27,33,34,35,36,37,38,39,42,43,44,45,46,47,48,49,50,51,59,60,65,68,95,116,],[-23,-22,-24,-25,-26,-27,45,49,45,-36,-37,-38,-39,65,45,-14,-15,-16,-17,-18,49,-19,-20,-21,-35,45,45,65,45,-30,45,]),'BOOLEAN':([18,19,20,21,22,23,26,27,33,34,35,36,37,39,42,43,44,45,46,47,48,49,50,51,59,60,68,95,116,],[-23,-22,-24,-25,-26,-27,46,50,46,-36,-37,-38,-39,46,-14,-15,-16,-17,-18,50,-19,-20,-21,-35,46,46,46,-30,46,]),'VARIABLE':([24,27,28,34,35,36,37,40,47,48,49,50,51,55,56,71,72,73,101,110,129,135,],[39,51,52,-36,-37,-38,-39,68,51,-19,-20,-21,-35,74,75,90,91,92,108,116,132,136,]),'LCOR':([25,30,31,52,53,],[40,55,56,71,72,]),'INCREASE':([28,],[53,]),'RPAREN':([41,42,43,44,45,46,48,49,50,51,58,67,69,70,77,78,80,96,99,105,107,108,109,115,127,130,131,132,134,136,137,138,],[69,-14,-15,-16,-17,-18,-19,-20,-21,-35,76,87,-34,89,-31,-32,95,102,106,111,113,114,115,119,130,133,-47,134,135,137,138,-40,]),'RCOR':([42,43,44,45,46,88,90,91,93,114,],[-14,-15,-16,-17,-18,96,97,98,100,118,]),'R_LLAVE':([61,62,63,64,65,66,84,85,86,],[81,82,83,-53,-55,-57,-54,-56,-58,]),'RANGE':([94,],[101,]),'CASE':([103,],[110,]),'RECUR':([112,],[117,]),'DOSPUNTOS':([120,125,],[124,-48,]),'INC':([122,],[126,]),'ELSE':([124,],[128,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucciones':([0,],[1,]),'asignacion':([0,],[2,]),'impresion':([0,59,123,],[3,77,127,]),'operacion_aritmetica1':([0,],[4,]),'condicional':([0,],[5,]),'vectores':([0,],[6,]),'conjuntos':([0,],[7,]),'defn':([0,],[8,]),'operacionesLogicas':([0,98,100,],[9,105,107,]),'sentenciaLoopRecur':([0,],[10,]),'doseq':([0,],[11,]),'cond_':([0,],[12,]),'sentencia_booleana':([0,32,],[13,59,]),'operador_comparadores':([0,15,57,],[14,33,33,]),'operacion':([15,],[27,]),'dato':([26,33,39,59,60,68,116,],[41,60,67,78,80,88,121,]),'valor':([27,47,],[47,70,]),'linecondition':([32,],[58,]),'expresionConjuntoEnteros':([38,64,],[61,84,]),'expresionConjuntoDouble':([38,65,],[62,85,]),'expresionConjuntoString':([38,66,],[63,86,]),'expresionDefnElse':([103,],[109,]),'expresionCase':([116,],[120,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucciones","S'",1,None,None,None),
  ('instrucciones -> asignacion','instrucciones',1,'p_instrucciones','clojure_sin.py',5),
  ('instrucciones -> impresion','instrucciones',1,'p_instrucciones','clojure_sin.py',6),
  ('instrucciones -> operacion_aritmetica1','instrucciones',1,'p_instrucciones','clojure_sin.py',7),
  ('instrucciones -> condicional','instrucciones',1,'p_instrucciones','clojure_sin.py',8),
  ('instrucciones -> vectores','instrucciones',1,'p_instrucciones','clojure_sin.py',9),
  ('instrucciones -> conjuntos','instrucciones',1,'p_instrucciones','clojure_sin.py',10),
  ('instrucciones -> defn','instrucciones',1,'p_instrucciones','clojure_sin.py',11),
  ('instrucciones -> operacionesLogicas','instrucciones',1,'p_instrucciones','clojure_sin.py',12),
  ('instrucciones -> sentenciaLoopRecur','instrucciones',1,'p_instrucciones','clojure_sin.py',13),
  ('instrucciones -> doseq','instrucciones',1,'p_instrucciones','clojure_sin.py',14),
  ('instrucciones -> cond_','instrucciones',1,'p_instrucciones','clojure_sin.py',15),
  ('instrucciones -> sentencia_booleana','instrucciones',1,'p_instrucciones','clojure_sin.py',16),
  ('instrucciones -> operador_comparadores','instrucciones',1,'p_instrucciones','clojure_sin.py',17),
  ('dato -> STRING','dato',1,'p_tipos_datos','clojure_sin.py',20),
  ('dato -> CHAR','dato',1,'p_tipos_datos','clojure_sin.py',21),
  ('dato -> ENTERO','dato',1,'p_tipos_datos','clojure_sin.py',22),
  ('dato -> FLOTANTE','dato',1,'p_tipos_datos','clojure_sin.py',23),
  ('dato -> BOOLEAN','dato',1,'p_tipos_datos','clojure_sin.py',24),
  ('valor -> ENTERO','valor',1,'p_valor','clojure_sin.py',27),
  ('valor -> FLOTANTE','valor',1,'p_valor','clojure_sin.py',28),
  ('valor -> BOOLEAN','valor',1,'p_valor','clojure_sin.py',29),
  ('operador_comparadores -> COMPARA_IGUAL','operador_comparadores',1,'p_operadoresComparadores','clojure_sin.py',33),
  ('operador_comparadores -> MENORQUE','operador_comparadores',1,'p_operadoresComparadores','clojure_sin.py',34),
  ('operador_comparadores -> MAYORQUE','operador_comparadores',1,'p_operadoresComparadores','clojure_sin.py',35),
  ('operador_comparadores -> MAYORIGUALQUE','operador_comparadores',1,'p_operadoresComparadores','clojure_sin.py',36),
  ('operador_comparadores -> MENORIGUALQUE','operador_comparadores',1,'p_operadoresComparadores','clojure_sin.py',37),
  ('operador_comparadores -> DIFERENTE','operador_comparadores',1,'p_operadoresComparadores','clojure_sin.py',38),
  ('asignacion -> LPAREN DEFICION VARIABLE dato RPAREN','asignacion',5,'p_asignacion','clojure_sin.py',41),
  ('asignacion -> LPAREN LET LCOR VARIABLE dato RCOR RPAREN','asignacion',7,'p_asignacion','clojure_sin.py',42),
  ('sentencia_booleana -> LPAREN operador_comparadores dato dato RPAREN','sentencia_booleana',5,'p_sentenciaBooleana','clojure_sin.py',45),
  ('linecondition -> sentencia_booleana impresion','linecondition',2,'p_linecondition','clojure_sin.py',48),
  ('linecondition -> sentencia_booleana dato','linecondition',2,'p_linecondition','clojure_sin.py',49),
  ('cond_ -> LPAREN COND linecondition RPAREN','cond_',4,'p_cond','clojure_sin.py',51),
  ('impresion -> LPAREN IMPRIMIR dato RPAREN','impresion',4,'p_impresion','clojure_sin.py',54),
  ('valor -> VARIABLE','valor',1,'p_valor_variable','clojure_sin.py',57),
  ('operacion -> MAS','operacion',1,'p_op_aritmetica1','clojure_sin.py',61),
  ('operacion -> MENOS','operacion',1,'p_op_aritmetica1','clojure_sin.py',62),
  ('operacion -> PRODUCTO','operacion',1,'p_op_aritmetica1','clojure_sin.py',63),
  ('operacion -> DIVISION','operacion',1,'p_op_aritmetica1','clojure_sin.py',64),
  ('operacionesLogicas -> LPAREN IF LPAREN MENORQUE VARIABLE ENTERO RPAREN LPAREN RECUR LPAREN INC LPAREN VARIABLE RPAREN RPAREN VARIABLE RPAREN RPAREN','operacionesLogicas',18,'p_operacionesLogicas','clojure_sin.py',67),
  ('operacion_aritmetica1 -> LPAREN operacion valor valor RPAREN','operacion_aritmetica1',5,'p_operacion_aritmetica1','clojure_sin.py',70),
  ('condicional -> LPAREN operacion valor valor RPAREN','condicional',5,'p_booleanos','clojure_sin.py',73),
  ('vectores -> VECTORES','vectores',1,'p_vectores','clojure_sin.py',76),
  ('doseq -> LPAREN DOSEQ LCOR VARIABLE LPAREN RANGE VARIABLE RPAREN RCOR LPAREN impresion RPAREN RPAREN','doseq',13,'p_doseq','clojure_sin.py',79),
  ('defn -> LPAREN DEFFUNCION VARIABLE LCOR VARIABLE RCOR LPAREN expresionDefnElse RPAREN RPAREN','defn',10,'p_defn','clojure_sin.py',82),
  ('defn -> LPAREN DEFFUNCION INCREASE LCOR VARIABLE RCOR operacionesLogicas RPAREN','defn',8,'p_defn','clojure_sin.py',83),
  ('expresionDefnElse -> CASE VARIABLE expresionCase DOSPUNTOS ELSE STRING','expresionDefnElse',6,'p_expresionDefnElse','clojure_sin.py',88),
  ('expresionCase -> dato STRING','expresionCase',2,'p_expresionCase','clojure_sin.py',92),
  ('conjuntos -> NUMERAL L_LLAVE expresionConjuntoEnteros R_LLAVE','conjuntos',4,'p_conjuntos','clojure_sin.py',95),
  ('conjuntos -> NUMERAL L_LLAVE expresionConjuntoDouble R_LLAVE','conjuntos',4,'p_conjuntos','clojure_sin.py',96),
  ('conjuntos -> NUMERAL L_LLAVE expresionConjuntoString R_LLAVE','conjuntos',4,'p_conjuntos','clojure_sin.py',97),
  ('sentenciaLoopRecur -> LPAREN LOOP LCOR VARIABLE ENTERO RCOR operacionesLogicas RPAREN','sentenciaLoopRecur',8,'p_sentenciaLoopRecur','clojure_sin.py',101),
  ('expresionConjuntoEnteros -> ENTERO','expresionConjuntoEnteros',1,'p_expresionConjuntoEnteros','clojure_sin.py',104),
  ('expresionConjuntoEnteros -> ENTERO expresionConjuntoEnteros','expresionConjuntoEnteros',2,'p_expresionConjuntoEnteros','clojure_sin.py',105),
  ('expresionConjuntoDouble -> FLOTANTE','expresionConjuntoDouble',1,'p_expresionConjuntoDouble','clojure_sin.py',109),
  ('expresionConjuntoDouble -> FLOTANTE expresionConjuntoDouble','expresionConjuntoDouble',2,'p_expresionConjuntoDouble','clojure_sin.py',110),
  ('expresionConjuntoString -> STRING','expresionConjuntoString',1,'p_expresionConjuntoString','clojure_sin.py',114),
  ('expresionConjuntoString -> STRING expresionConjuntoString','expresionConjuntoString',2,'p_expresionConjuntoString','clojure_sin.py',115),
]
