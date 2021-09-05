from tkinter import *
from automata import *
def iniciar(frame: Frame, e: Entry, b:Button, miAutomata: Automata): 
    x=20
    y=20
    Label(frame, text="Nombre: ", padx=x, pady=y, font=miAutomata.font).grid(row=0, column=0)
    Label(frame, text=miAutomata.nombre, padx=x, pady=y, font=miAutomata.font).grid(row=0, column=1)
    Label(frame, text="Matricula", padx=x, pady=y, font=miAutomata.font).grid(row=1, column=0)
    Label(frame, text=miAutomata.matricula, padx=x, pady=y, font=miAutomata.font).grid(row=1, column=1)
    Label(frame, text="Alfabeto:", padx=x, font=miAutomata.font).grid(columnspan=2)
    sigma = miAutomata.sigma
    Label(frame, text=sigma, font=miAutomata.font).grid(columnspan=2)
    Label(frame, text="Reglas: ", pady=5, font=miAutomata.font).grid(columnspan=2)
    for r in reglas: 
        Label(frame, text=r, pady=5, font=miAutomata.font).grid(columnspan=2)
    Label(frame, text="Ingrese una cadena: ", pady=y/2, font=miAutomata.font).grid(columnspan=2)
    e.grid(columnspan=2, pady=y)
    b.grid(columnspan=2)
def continuar(resultado: Label, si: Button, no: Button, pregunta: Label, b: Button): 
    b.configure(state="active")
    resultado.configure(text="")
    si.destroy()
    no.destroy()
    pregunta.destroy()

def click(e: Entry, resultado: Label, frame: Frame, b: Button, root: Tk):
    miAutomata.actualizar_cadena(e.get())
    if miAutomata.q0(): 
        resultado.configure(text="Cadena válida")
    else: 
        resultado.configure(text="Cadena inválida")
    resultado.grid(columnspan=2)
    b.configure(state="disabled")
    si = Button(frame, text="Sí", padx=20, font=miAutomata.font)
    no = Button(frame, text="No", padx=20, font=miAutomata.font)
    pregunta = Label(frame, text="¿Desea continuar?", font=miAutomata.font)
    pregunta.grid(columnspan=2)
    si.grid(row= 16,column=0, pady=10)
    no.grid(row=16, column=1, pady=10)

    si.configure(command=lambda: continuar(resultado, si, no, pregunta, b))
    no.configure(command=lambda: root.destroy())

    pass
if __name__=="__main__": 
    miAutomata = Automata()
    root = Tk()
    root.title("TA_032_EA1_E1")
    Label(root, text="Este programa acepta una cadena y decide si es válida dentro del alfabeto generado por el siguiente nombre y matrícula: ", font=miAutomata.font, pady=10).pack()
    frame = Frame(root)
    frame.pack()
    e=Entry(frame, font=miAutomata.font)
    resultado = Label(frame, font=miAutomata.font)
    b=Button(frame, text="Ingresar cadena", font=miAutomata.font, command=lambda: click(e, resultado, frame, b, root), pady=10, padx=10)
    iniciar(frame, e, b, miAutomata)
    resultado.grid(columnspan=2)
    root.mainloop()