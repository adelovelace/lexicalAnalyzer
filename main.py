import clojure_sin
from datetime import datetime


log_file = open('log.txt', 'a')

while True:
    try:
        s = input('calc > ')
        prueba = "Prueba: " + datetime.today().strftime("%d/%m/%Y") + " " + datetime.now().strftime("%H:%M:%S") + '\n' + 'calc > ' + s + '\n'
        log_file.writelines(prueba)
    except EOFError:
        break
    if not s: continue
    clojure_sin.validaRegla(s)




