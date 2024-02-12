#Clase
"""
class Persona:
    #aributo de clase
    viva = True

    #Constructor de la clase
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        #atributo protegido
        self._apellido_paterno
    
    #Método especial de python, que indica el formato de impresión en pantalla, viene muy de la mano con print()
    def __str__(self) -> str:
        return "mi nombre es "+self.nombre+" mi edad es "+str(self.edad)+" y soy "+self.genero

#Objeto

#Instanciacion: es cuando se crea la referencia en memoria

persona1 = Persona("Lau", 20, "mujer")
persona2 = Persona("Arturo", 40, "hombre")
persona3 = Persona("Juan", 28, "hombre")


print(persona1)
print(persona3)

"""


class Animal:

    def __init__(self, nombre, edad, identificador) -> None:
        self.nombre = nombre
        self._edad = edad
        self.__identificador = identificador

    def get_identificador(self):
        return self.__identificador
    
    def set_identificador(self,iden):
        self.__identificador = iden
    
    def __str__(self) -> str:
        return "mi nombre es "+self.nombre+" mi edad es "+str(self._edad)+" y mi identificador es "+self.__identificador

class Perro(Animal):

    #constructor de la clase hija (Perro)
    def __init__(self, nombre, edad, identificador, raza) -> None:
        #Constructor de la clase padre (Animal)
        super().__init__(nombre, edad, identificador)
        self.raza = raza

    def __str__(self) -> str:
        return "mi nombre es "+self.nombre+" mi edad es "+str(self._edad)+" son de raz "+self.raza

class Gato(Animal):
    #constructor de la clase hija (Gato)
    def __init__(self, nombre, edad, identificador,  num_camada) -> None:
        #Constructor de la clase padre (Animal)
        super().__init__(nombre, edad, identificador)
        self.num_camada = num_camada

    def __str__(self) -> str:
        return "mi nombre es "+self.nombre+" mi edad es "+str(self._edad)+" numero de camada "+str(self.num_camada)

animal1 = Animal("mamifero", 2, "abc")
perro1 = Perro("mamifero", 4, "abd", "bully")
gato1 = Gato("mamifero", 3, "azzz", 2)

#El metodo set modifica el valor del atributo privado self.__identificador
animal1.set_identificador("yyyy")
#El metodo get obtiene el valor del atributo privado self.__identificador
print(animal1.get_identificador())


print(animal1)
print(perro1)
print(gato1)












