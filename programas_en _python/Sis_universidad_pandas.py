from random import randint
from datetime import datetime
import csv
import pandas as pd


class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.id = randint(1,100)
        self.nombre = nombre
        self.apellido = apellido
    
    def  __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.id} {self.nombre} {self.apellido}"
    
class Curso:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def __str__(self) -> str:
        return self.nombre
    
class Estudiante(Persona):
    def __init__(self, nombre, apellido) -> None:
        super().__init__(nombre, apellido)
        fecha = datetime.now() #fecha es una variable local  mas no de instancia
        self.fecha_registro = fecha.strftime("%Y-%m-%d %H:%M")
        self.cursos = [] #Agregación

    def __str__(self) -> str:
        cursos_str = ', '.join(str(c) for c in self.cursos)
        return super().__str__() + " " + str(self.fecha_registro) + " " + cursos_str
    
    def agregar_curso(self, nombre_curso):
        #Relación de Composición
        curso = Curso(nombre_curso) #creamos instacia de un cursdo cada vez que se llame a este método
        self.cursos.append(curso)
    
    """
    def guardar_estudiante(self):
        #encabezados = ["ID", "Nombre", "Apellido", "Fecha_registro", "Cursos"]
        with open('estudiantes_uni.csv', 'a', newline='') as archivo:
            archivo_csv = csv.writer(archivo)
            cursos_csv = ', '.join(str(c) for c in self.cursos)
            archivo_csv.writerow([self.id, self.nombre, self.apellido, self.fecha_registro, cursos_csv])
    """

class Universidad:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.estudiantes = []
        self.df = pd.DataFrame(columns=["ID", "Nombre", "Apellido", "Fecha_registro", "Cursos"])
    
    def agregar_estudiante(self, estudiante):
        #Relacion de agregación
        self.estudiantes.append(estudiante)

    def __str__(self) -> str:
        estudiates_str = ', '.join(str(estudiante) for estudiante in self.estudiantes)#estudiates_str es una variable local y no una de instancia
        return f"{self.nombre}\n{estudiates_str}"
    
    def guardar_datos(self):

        for estudiante in self.estudiantes:
            cursos_csv = ", ".join(str(c) for c in estudiante.cursos)
            self.df = self.df._append({"ID":estudiante.id, "Nombre":estudiante.nombre, "Apellido":estudiante.apellido, "Fecha_registro":estudiante.fecha_registro, "Cursos":cursos_csv},ignore_index=True)
        
        self.df.to_csv("Estudiante_datos.csv")
    
    def buscar(self, pos):
        try:
            data = pd.read_csv("Estudiante_datos.csv")
            for indi in self.df.index:
                if indi == pos:
                    return True, data
        except FileNotFoundError:
            print("El archivo CSV NO Existe!")
        return False, data
    
    def setNombre(self, indi, nombre):
        flag, data = self.buscar(indi)
        if flag:
            data.iloc[indi, data.columns.get_loc("Nombre")] = nombre
            data.to_csv("Estudiante_datos.csv")

    def buscarEstudiante(self, pos):
        flag, data = self.buscar(pos)
        if flag:
            return str(data.iloc[pos])

    def listarEstudiantes(self):
        try:
            data = pd.read_csv("Estudiante_datos.csv")
            for indi in self.df.index:
                print(str(data.iloc[indi]))
        except FileNotFoundError:
            print("No se puede listar, ya que no se encuentra el archivo solicitado!")


uacm = Universidad("UACM")

es1 = Estudiante("juan", "Herrera")
es1.agregar_curso("POO")
es1.agregar_curso("Analisis real")

es2 = Estudiante("Pedro", "reyes")
es2.agregar_curso("Estructura de datos")
es2.agregar_curso("Analisis de algooritmo")
es2.agregar_curso("Arquitectura de software")

uacm.agregar_estudiante(es1)
uacm.agregar_estudiante(es2)
uacm.guardar_datos()

print(es1)
print(es2)

#pos = int(input("Ingresa El indice a buscar: "))
uacm.setNombre(1, "Panfilo Anastasio")
#print(uacm.buscarEstudiante(pos))
uacm.listarEstudiantes()






