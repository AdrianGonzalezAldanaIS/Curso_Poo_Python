"""
class Numeros:
    
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def __init__(self, a, b, c = 0) -> None:
        self.a = a
        self.b = b
        self.c = c

    def impresion(self):
        return "A vale "+str(self.a)+ " B vale: "+str(self.b)+" C Vale: "+str(self.c)
    
    def __str__(self) -> str:
        return f"A vale {self.a}, y B vale {self.b}"



#num = Numeros(1, 2)
#print(num)
num2 = Numeros(1, 2, 3)
print(num2)
num3 = Numeros(4, 5)
print(num3.impresion())

"""

class Numeros:
    #constructor que emula la sobre carga de métoos con el argumento opcional (C = 0)
    def __init__(self, a, b, c = 0) -> None:
        self.a = a
        self.b = b
        self.c = c

    def calcular(self, a, b):
        return a + b
    

    
    def impresion(self):
        return "A vale "+str(self.a)+ " B vale: "+str(self.b)+" C Vale: "+str(self.c)
    
    def __str__(self) -> str:
        return f"A vale {self.a}, y B vale {self.b}"

class Hija(Numeros):
    #Sobre escritura
    #En la clase padre esta implementado, pero en la clase hija se puede sobre escribir, incluso añadiendole más argumentos
    def calcular(self, a, b):
        return a * b


hija = Hija(1,2,3)

print(hija.calcular(3,4))

class Sobrecarga2:
    def __init__(self, *valores) -> None: ##argumentos *args
        self.valor = valores
        pass
    
    def suma(self):
        self.sum = 0

        for numero in self.valor:
            self.sum = self.sum + numero
        print("Suma:", self.sum)

sob = Sobrecarga2(1)
print(sob.suma())
