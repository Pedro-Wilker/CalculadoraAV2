import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def bin_to_dec():
    binary = entry.get()
    try:
        decimal = int(binary, 2)
        messagebox.showinfo("Resultado", f"Binário: {binary}\nDecimal: {decimal}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Por favor, insira um número binário válido.")

def dec_to_bin():
    decimal = entry.get()
    try:
        decimal = int(decimal)
        binary = bin(decimal).replace("0b", "")
        messagebox.showinfo("Resultado", f"Decimal: {decimal}\nBinário: {binary}")
    except ValueError:
        messagebox.showerror("Erro", "Entrada inválida! Por favor, insira um número decimal válido.")

def open_calculator():
    calc_win = tk.Toplevel(app)
    calc_win.title("Calculadora Normal")
    calc_win.geometry("400x600")
    calc_win.configure(bg="white")

    def append_to_expression(symbol):
        expression.set(expression.get() + str(symbol))

    def clear_expression():
        expression.set("")

    def calculate():
        try:
            result = eval(expression.get())
            expression.set(result)
        except Exception:
            expression.set("Erro")

    expression = tk.StringVar()
    
    
    display = ttk.Entry(calc_win, textvariable=expression, font=("Helvetica", 20), justify='right')
    display.pack(pady=10, padx=10, fill="both")

   
    buttons_frame = ttk.Frame(calc_win)
    buttons_frame.pack(pady=10, padx=10, fill="both")

    buttons = [
        '7', '8', '9', '/', 
        '4', '5', '6', '*', 
        '1', '2', '3', '-', 
        '0', '.', '=', '+'
    ]

    row = 0
    col = 0
    for button in buttons:
        action = lambda x=button: append_to_expression(x) if x != '=' else calculate()
        ttk.Button(buttons_frame, text=button, command=action).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        col += 1
        if col > 3:
            col = 0
            row += 1

    ttk.Button(buttons_frame, text="C", command=clear_expression).grid(row=row, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

    for i in range(4):
        buttons_frame.grid_columnconfigure(i, weight=1)
    for i in range(row+1):
        buttons_frame.grid_rowconfigure(i, weight=1)

app = tk.Tk()
app.title("Calculadora de Conversão de Bases")
app.geometry("400x400")
app.configure(bg="white")

style = ttk.Style()
style.configure("TLabel", background="white", foreground="black", font=("Helvetica", 12))
style.configure("TButton", background="#3498db", foreground="black", font=("Helvetica", 10), padding=10)
style.map("TButton", foreground=[('active', 'black')], background=[('active', '#2980b9')])

frame = ttk.Frame(app, padding="10")
frame.pack(expand=True)

ttk.Label(frame, text="Digite o número:").pack(pady=10)
entry = ttk.Entry(frame, font=("Helvetica", 14))
entry.pack(pady=10)

ttk.Button(frame, text="Binário para Decimal", command=bin_to_dec).pack(pady=5)
ttk.Button(frame, text="Decimal para Binário", command=dec_to_bin).pack(pady=5)
ttk.Button(frame, text="Calculadora Normal", command=open_calculator).pack(pady=5)

app.mainloop()