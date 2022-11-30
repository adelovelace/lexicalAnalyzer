from clojure_lex import input_sentence
from clojure_sin import validaRegla
import tkinter as tk
from tkinter import ttk

def take_input(screen_input, table):
    INPUT = screen_input.get("1.0", "end-1c")

    for result in input_sentence(INPUT):
        tuple_data = (result.value, result.type, result.lineno, result.lexpos)
        table.insert('', 'end', text="1", values=tuple_data)

def show_parser(screen_input):
    INPUT = screen_input.get("1.0", "end-1c")
    text_result = validaRegla(INPUT)
    parser_entry.delete('1.0', tk.END)
    parser_entry.insert(tk.END, text_result)


def both(input, lexico):
    show_parser(input)
    for i in lexico.get_children():
        lexico.delete(i)

    take_input(input, lexico)

def clear_all(input_text, table1):
    input_text.delete('1.0', tk.END)
    parser_entry.delete('1.0', tk.END)
    for i in table1.get_children():
        table1.delete(i)


window = tk.Tk()
window.title("Clojure Analyzer")
window.geometry("930x605")

# INPUT CODE SECTION
etiqueta_input = ttk.Label(text="Code")
etiqueta_input.grid(row=0, column=0, columnspan=6)

pantalla = tk.Text(window,
                   width=60,
                   height=20,
                   bg="#45458B",
                   borderwidth=0,
                   font=('Courier', 12))

pantalla.grid(row=1, columnspan=6, padx=(10, 0))

# LEXICAL ANALIZER VIEWER SECTION
etiqueta_lexico = ttk.Label(text="Lexical Analyzer")
etiqueta_lexico.grid(row=0, column=7)

lexico_table = ttk.Treeview(window, column=("Lexema", "Token", "Linea", "Columna"), show='headings')
lexico_table.column("# 1", anchor=tk.CENTER, stretch=tk.NO, width=100)
lexico_table.heading("# 1", text="Lexema")
lexico_table.column("# 2", anchor=tk.CENTER, stretch=tk.NO, width=100)
lexico_table.heading("# 2", text="Token")
lexico_table.column("# 3", anchor=tk.CENTER, stretch=tk.NO, width=100)
lexico_table.heading("# 3", text="Linea")
lexico_table.column("# 4", anchor=tk.CENTER, stretch=tk.NO, width=100)
lexico_table.heading("# 4", text="Columna")

lexico_table.grid(row=1, column=7, sticky=tk.NSEW, padx=(0, 10))

# PARSER SECTION
etiqueta_parser = ttk.Label(text="Parser", justify=tk.LEFT)
etiqueta_parser.grid(row=3, column=0, columnspan=8, sticky=tk.NSEW, padx=(10, 0))

parser_label = tk.Label(window, anchor='nw', justify='left', text="", font=('Arial 12'), fg='#FFFFF8', bg="#3B3B3B", height=20)
v = tk.Scrollbar(window)
parser_entry = tk.Text(window, width = 15, height = 21.49, wrap = tk.NONE, yscrollcommand = v.set)

parser_entry.grid(row=4, column=0, sticky=tk.NSEW, columnspan=9, padx=(10, 10), pady=(0, 10))

# BUTTONS
middle_frame = tk.Frame(width=80)
middle_frame.grid(row=1, column=6)

tk.Button(middle_frame, text="Lexical", command=lambda: take_input(pantalla, lexico_table)).grid(row=1)
tk.Button(middle_frame, text="Parser", command=lambda: show_parser(pantalla)).grid(row=2)
tk.Button(middle_frame, text="Both", command=lambda: both(pantalla, lexico_table)).grid(row=3)
tk.Button(middle_frame, text="Clear", command=lambda: clear_all(pantalla, lexico_table)).grid(row=4)

window.mainloop()
