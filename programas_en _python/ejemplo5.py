

"""
class Profesor:

    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def __str__(self):
        return f"{self.nombre}"

class Estudiante:
    def __init__(self, nombre, profesor) -> None:
        self.nombre = nombre
        self.profesor = profesor
    
    def __str__(self):
        return f"Estudiante: {self.nombre} y nombre de profesor: {self.profesor}"
    

profe1 = Profesor("Alberto")
alumno1 = Estudiante("jorge", profe1)
alumno2 = Estudiante("jorge", profe1)
alumno3 = Estudiante("jorge", profe1)

print(alumno1)


class Empleado:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    def __str__(self):
        return self.nombre
    
class Departamento:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.empleados = []
    
    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        #print(str(self.empleados))

    def __str__(self) -> str:
        return f"Nombre del departamento: {self.nombre}, empleado: {self.empleados.__str__()}"

emp1 = Empleado("Andre")
emp2 = Empleado("Maria de los Angeles")
emp3 = Empleado("Joel")

#print(emp1)
rh = Departamento("Recursos Inhumanos")
rh.agregar_empleado(emp1)
rh.agregar_empleado(emp2)
rh.agregar_empleado("emp3")
print(rh)
"""
class Motor:
    def __init__(self, serie) -> None:
        self.serie = serie

    def __str__(self) -> str:
        return self.serie

class Neumatico:
    def __init__(self, marca) -> None:
        self.marca = marca
    
    def __str__(self) -> str:
        return self.marca

class Coche:
    def __init__(self, marca, modelo, anio, num_llantas) -> str:
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.motor = Motor("Ab123")
        self.llantas = [Neumatico(marca) for i in range(num_llantas)]
    
    def __str__(self) -> str:
        str_llantas = ', '.join(str(n) for n in self.llantas)
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Amio: {self.anio}, Motor: {self.motor}, LLanta: {str_llantas}"


coche1 = Coche("Ford", "Mustang", 2020, 4)
coche2 = Coche("Ford", "Torton", 2050, 8)

print(coche1)
print(coche2)
