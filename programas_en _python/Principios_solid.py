#Principio de Abierto Cerrado
#Antes de aplicar el principio:
"""
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name
    

animales = [Animal("leon"),
            Animal("mouse")]


def animal_sonido(animales):
    for animal in animales:
        if animal.name == 'leon':
            print("grrrrr")
        elif animal.name == 'mouse':
            print("squik")

animal_sonido(animales)

#Aplicando el principio:

class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def get_name(self):
        return self.name
    
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'

class Snake(Animal):
    def make_sound(self):
        return 'hiss'
#Instanciias de animales
leon = Lion("Estepario")
raton = Mouse("Del campo")
serpiente = Snake("De cascabel")
#Lista de animales
animales = [leon, raton, serpiente]

def animal_sonido(animales):
    for animal in animales:
        print(animal.make_sound())

animal_sonido(animales)


#Principio de Sustitución de Liskov

class Animal:
    def comer(self):
        print("El animal esta comiendo")

class Perro (Animal):
    def comer(sel):
        print("El PErro esta comiendo")

class Gato(Animal):
    def comer(sel):
        print("El Gato esta comiendo")

def alimentar_amimal(animal):
    animal.comer()

perro = Perro()
gato = Gato()
animal = Animal()

alimentar_amimal(perro)
alimentar_amimal(gato)
alimentar_amimal(animal)
"""


#Principio de Segregación de Interfaces (Clases Abstractas)
"""
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def andar(self):
        pass

    @abstractmethod
    def volar(self):
        pass

class Aeronave(Vehiculo):
    def andar(self):
        print("Rodando")

    def volar(self):
        print("Volando")

class Carro(Vehiculo):
    def andar(self):
        print("Andando")

    def volar(self):
        raise Exception('El carro no puede volar')

from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def andar(self):
        pass

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Aeronave(Vehiculo, Volador):
    def andar(self):
        print("La aeronave esta Rodando")

    def volar(self):
        print("La aeronave esta Volando")

class Carro(Vehiculo):
    def andar(self):
        print("El carro esta Andando")

avion = Aeronave()
avion.andar()
avion.volar()

bocho = Carro()
bocho.andar()

from abc import ABC, abstractmethod
import math
class Cal_basica(ABC):
    @abstractmethod
    def suma(self, a, b):
        pass

    @abstractmethod
    def resta(self, a, b):
        pass

class Cal_cient(ABC):

    @abstractmethod
    def seno(self, a):
        pass

    @abstractmethod
    def cos(self, a):
        pass

class CalculadoraCientifica(Cal_basica, Cal_cient):
    def suma(self,a ,b):
        return a+b

    def resta(self, a, b):
        return a-b

    def seno(self, a):
        return math.sin(a)
    
    def cos(self, a):
        return math.cos(a)
    

cal = CalculadoraCientifica()
print(cal.resta(10, 3))
print(cal.suma(10, 3))
print(cal.seno(3))
print(cal.cos(3))
"""


#Principio de Inversion de Dependencias


from abc import ABC, abstractmethod

class Motor(ABC):
    
    @abstractmethod
    def encender(self):
        pass
    
    @abstractmethod
    def apagar(self):
        pass

class Coche:
    
    def __init__(self, motor: Motor):
        self.motor = motor
        
    def encender_coche(self):
        self.motor.encender()
    
    def apagar_coche(self):
        self.motor.apagar()

class MotorGasolina(Motor):
    
    def encender(self):
        print("Encendiendo motor de gasolina...")
    
    def apagar(self):
        print("Apagando motor de gasolina...")

class MotorElectrico(Motor):
    
    def encender(self):
        print("Encendiendo motor eléctrico...")
    
    def apagar(self):
        print("Apagando motor eléctrico...")

class MotorDiesel(Motor):
    def encender(self):
        print("Encendiendo motor diesel...")
    
    def apagar(self):
        print("Apagando motor dieles...")

motor_gasolina = MotorGasolina()
coche_gasolina = Coche(motor_gasolina)

coche_gasolina.encender_coche()
coche_gasolina.apagar_coche()
print()
motor_electrico = MotorElectrico()
coche_electrico = Coche(motor_electrico)
coche_electrico.encender_coche()
coche_electrico.apagar_coche()
print()
motor_diesel = MotorDiesel()
coche_diesel = Coche(motor_diesel)
coche_diesel.encender_coche()
coche_diesel.apagar_coche()






