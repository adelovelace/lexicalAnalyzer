import clojure_sin

while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    clojure_sin.validaRegla(s)
