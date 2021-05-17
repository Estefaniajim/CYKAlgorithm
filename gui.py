import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import main
from tkinter import ttk

def openFile():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    advertencia("Escriba los siguientes datos separados por un enter. 1. La cadena, 2. el numero de reglas "
                "gramaticales, 3. Todas las reglas gramaticales separadas por un enter. ")
    window.title(f"Algoritmo de CYK - {filepath}")

def saveFile():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Algoritmo de CYK - {filepath}")
    getInfoUser(filepath)

def resultados(msg):
    popup = tk.Tk()
    popup.wm_title("Resultado")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Cerrar", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def advertencia(msg):
    popup = tk.Tk()
    popup.wm_title("Recuerde")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Cerrar", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def getInfoUser(filepath):
    with open(filepath) as file:
        lines = file.read().splitlines()
    w = lines[0]
    n = int(lines[1])
    rules = {}
    memo = []
    for rule in lines[2:2+n]:
        rule = rule.split()
        if rule[1] not in rules:
            rules[rule[1]] = [rule[0]]
        else:
            rules[rule[1]].append(rule[0])
        if rule[2] not in rules:
            rules[rule[2]] = [rule[0]]
        else:
            rules[rule[2]].append(rule[0])
    for i in range(len(w)):
        row = []
        for j in range(len(w)):
            row.append(0)
        memo.append(row)
    result = main.CYK(w, rules, memo)
    if result:
        resultados(" Si pertenece, su arbol es: " + str(memo))
    else:
        resultados(" No pertenece, su arbol es: " + str(memo))

window = tk.Tk()
window.title("Algoritmo de CYK")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Abrir", command=openFile)
btn_save = tk.Button(fr_buttons, text="Guardar...", command=saveFile)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
