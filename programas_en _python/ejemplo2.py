"""
class Motor:
    #publicos
    #protegidos
    #privatdos

    #Inicializacion de los atributos de instancia
    def __init__(self, id_motor, tipo_combustible) -> None:#constructor de la clase Motor
        self.id_motor = id_motor#atributos de instacia - publico
        self.__tipo_combustible = tipo_combustible #atributo privado
        
    #-------------- Métodos ---------------------------------
    def get_id_motor(self):
        return self.id_motor
    # metodo para acceder al valor del atributo privado self__tipo_combustible
    def get_tipo_motor(self):
        return self.__tipo_combustible

    #Sobre escritura del m´étodo especial str()
    def __str__(self) -> str:
        return "El id del motro es "+self.id_motor+" El tipo de combustible es: "+self.__tipo_combustible
    

#instancia de objetos
motor1 = Motor("abc","Diessel")
motor2 = Motor("def","Gasolina")
motor3 = Motor("ghi","Gas")
##print(type(motor1))
print(motor1)
print(motor1.get_id_motor())
print("Motor 2")
print(motor2.get_id_motor())
#llamando a atributos publicos
print(motor1.id_motor)
#LLamando a atributos privados
print(motor1._Motor__tipo_combustible)
print(motor1.get_tipo_motor())

"""
#Clase padre 1
class Reptiliano:
    def __init__(self, categoria) -> None:
        self.categoria = categoria
    
    def __str__(self) -> str:
        return "Categoria: "+self.categoria
#Clase padre 2
class Persona:

    def __init__(self, id_persona) -> None:
        self.id_persona = id_persona
    pass

    def __str__(self) -> str:
        return "Mi Id: "+self.id_persona
#Clase hija que hereda de la clase Padre 1 y 2
class Estudiante(Reptiliano, Persona):

    def __init__(self,id_persona, categoria, nombre) -> None: #constructor de la clase Estudiante (clase hija)
        super().__init__(id_persona)#construcor de la clase Persona (Padre)
        super().__init__(categoria)#construcor de la clase Reptiliano (Padre)
        
        self.nombre = nombre

    def __str__(self) -> str:
        return "Mi categoria es: "+self.categoria+"Mi nombre es: "+self.nombre


#objeto de la clase Persona (padre)
persona1 = Persona("123")
print(persona1)

#objeto Estudiante (hijo) que hereda de la clase Persona (padre)
estu1 = Estudiante("123", "plat1", "Pedro")
print(estu1)

