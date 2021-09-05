from random import randrange

nombres = ["kenneth martin rodriguez garcia", "maria fernanda guerra reyes", "roberto tadeo cuellar gracia", "alejandra marisol cantu ruiz"]
matriculas = ["1916780", "1927750", "1732780", "1596437"]
reglas=[
    "1.- El primer símbolo debe ser un dígito",
    "2.- Puede contener cualquier conmbinaciónde letras y dígitos intermedia, válidos en el alfabeto", 
    "3.- La cadena debe contener las iniciales del nombre de manera consecutica, al menos una vez", 
    "4.- Debe contener como últimos símbolos un punto seguido del número de matrícula", 
    "5.- Puede aceptar puntos intermedios, pero no de forma consecutiva"
]
class Automata(): 
    def __init__(self) -> None:
        num = randrange(0, len(nombres))
        self.pos = 0
        self.sigma = ["."]
        self.iniciales = ""
        self.cadena = ""
        self.nombre = nombres[num]
        self.matricula = matriculas[num]
        self.font = ('bold', 15)
        for letra in self.nombre:
            if letra not in self.sigma and letra != " ": 
                self.sigma.append(letra)
        for inicial in self.nombre.split(" "): 
            self.iniciales += inicial[0]
        for digito in self.matricula: 
            if digito not in self.sigma: 
                self.sigma.append(digito)

    def actualizar_cadena(self, nueva_cadena: str): 
        self.cadena = nueva_cadena
        self.pos = 0
    
    def q0(self)->bool: 
        print("q0->")
        if self.cadena != "": 
            if self.cadena[0] in self.sigma and self.cadena[0].isdigit():
                return self.q1()
        return self.fallo()

    def q1(self)->bool: 
        print("q1->")
        self.pos += 1
        if self.pos < len(self.cadena):
            if self.cadena[self.pos] == self.iniciales[0]:
                return self.q2()
            elif self.cadena[self.pos] == ".": 
                return self.q3()
            elif self.cadena[self.pos] in self.sigma: 
                return self.q1()
        return self.fallo()

    def q2(self, i=1)->bool: 
        print("q2->")
        self.pos += 1
        if self.pos < len(self.cadena):
            if i == len(self.iniciales):
                if self.cadena[self.pos] == ".": 
                    return self.q5()
                elif self.cadena[self.pos] in self.sigma: 
                    return self.q4()
            else: 
                if self.cadena[self.pos] == self.iniciales[i]: 
                    return self.q2(i+1)
                elif self.cadena[self.pos] == self.iniciales[0]: 
                    return self.q2()
                elif self.cadena[self.pos] == ".": 
                    return self.q3()
                elif self.cadena[self.pos] in self.sigma: 
                    return self.q1()
        return self.fallo()
    #Checar punto
    def q3(self)->bool: 
        print("q3->")
        self.pos += 1
        if self.pos < len(self.cadena): 
            if self.cadena[self.pos] == ".": 
                return self.fallo()
            elif self.cadena[self.pos] == self.iniciales[0]: 
                return self.q2()
            elif self.cadena[self.pos] in self.sigma: 
                return self.q1()
        return self.fallo()

    def q4(self)->bool: 
        print("q4->")
        self.pos += 1
        if self.pos < len(self.cadena):
            if self.cadena[self.pos] == ".": 
                return self.q5()
            elif self.cadena[self.pos] in self.sigma: 
                return self.q4()
        return self.fallo()

    def q5(self)->bool: 
        print("q5->")
        self.pos+=1
        if self.pos < len(self.cadena): 
            if self.cadena[self.pos] == ".": 
                return self.fallo()
            elif self.cadena[self.pos] == self.matricula[0]: 
                return self.q6()
            elif self.cadena[self.pos] in self.sigma: 
                return self.q4()
        return self.fallo()

    def q6(self, i=1)->bool: 
        print("q6->")
        self.pos+=1
        if i == len(self.matricula): 
            return self.q7()
        elif self.pos < len(self.cadena):
            print("Pos: "+str(self.pos))
            print("i: "+str(i))
            if self.cadena[self.pos] == self.matricula[i]: 
                return self.q6(i+1)
            elif self.cadena[self.pos] == ".": 
                return self.q5()
            elif self.cadena[self.pos] in self.sigma: 
                return self.q4()
        return self.fallo()
    
    def q7(self)->bool: 
        print("q7")
        if self.pos == len(self.cadena): 
            return self.exito()
        elif self.cadena[self.pos] == ".": 
            return self.q5()
        elif self.cadena[self.pos] in self.sigma: 
            return self.q4()
        return self.fallo()
        
    def exito(self)->bool: 
        print("Éxito")
        return True
    def fallo(self)->bool: 
        print("Fallo")
        return False