import tkinter as tk
from tkinter import ttk

def Take_input(screen_input):
    INPUT = screen_input.get("1.0", "end-1c")
    # lexer.input(INPUT)
    # getTokens(lexer)

    print(INPUT)

window = tk.Tk()
window.title("Clojure Analyzer")
window.geometry("930x530")


#INPUT CODE SECTION
etiqueta_input = ttk.Label(text="Code")
etiqueta_input.grid(row=0, column=0,columnspan=6)

pantalla = tk.Text(window,
               width=60,
               height=20,
               bg="#45458B",
               borderwidth=0,
               font=('Courier', 12))

pantalla.grid(row=1, columnspan=6, padx=(10,0))

#BUTTONS
middle_frame = tk.Frame(width=80)
middle_frame.grid(row=1, column=6)

lexical_button = tk.Button(middle_frame, text = "Lexical").grid(row=1)
parser_button = tk.Button(middle_frame, text = "Parser", command= lambda:Take_input(pantalla)).grid(row=2)

# LEXICAL ANALIZER VIEWER SECTION
etiqueta_lexico = ttk.Label(text="Lexical Analyzer")
etiqueta_lexico.grid(row=0, column=7)

lexico_table = ttk.Treeview(window, column=("Lexema", "Token", "Linea", "Columna"), show='headings')
lexico_table.column("# 1", anchor=tk.CENTER, stretch=tk.NO, width=100)
lexico_table.heading("# 1", text="Lexema")
lexico_table.column("# 2", anchor=tk.CENTER,stretch=tk.NO, width=100)
lexico_table.heading("# 2", text="Token")
lexico_table.column("# 3", anchor=tk.CENTER, stretch=tk.NO, width=100)
lexico_table.heading("# 3", text="Linea")
lexico_table.column("# 4", anchor=tk.CENTER, stretch=tk.NO, width=100)
lexico_table.heading("# 4", text="Columna")

lexico_table.insert('', 'end', text="1", values=('Amit', 'Kumar', '17701','17701'))
lexico_table.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
lexico_table.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
lexico_table.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))
lexico_table.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
lexico_table.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
lexico_table.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))
lexico_table.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
lexico_table.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
lexico_table.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))
lexico_table.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
lexico_table.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
lexico_table.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))
lexico_table.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
lexico_table.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
lexico_table.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))
lexico_table.insert('', 'end', text="1", values=('Ankush', 'Mathur', '17702'))
lexico_table.insert('', 'end', text="1", values=('Manisha', 'Joshi', '17703'))
lexico_table.insert('', 'end', text="1", values=('Shivam', 'Mehrotra', '17704'))

lexico_table.grid(row=1, column=7, sticky=tk.NSEW, padx=(0,10))

#PARSER SECTION
etiqueta_sintactico = ttk.Label(text="Parser",justify=tk.LEFT)
etiqueta_sintactico.grid(row=3, column=0,columnspan=8, sticky=tk.NSEW, padx=(10,0))

parser_table = ttk.Treeview(window, column=("Estructura", "Detalle"), show='headings')
parser_table.column("# 1", anchor=tk.CENTER, stretch=tk.NO,width=300)
parser_table.heading("# 1", text="Estructura")
parser_table.column("# 2", anchor=tk.CENTER,stretch=tk.NO,width=600)
parser_table.heading("# 2", text="Detalle")

parser_table.insert('', 'end', text="1", values=('Amit', 'Kumar'))

parser_table.grid(row=4, column=0, sticky=tk.NSEW, columnspan=9, padx=(10,10), pady=(0,10))




window.mainloop()