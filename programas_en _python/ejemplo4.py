"""
def imprimir_datos(nombre, *arr, **dic_arr):
    print(f"Nombre: {nombre}")

    for ar in arr:
        print(f"Valor: {ar}")
    for llave, valor in dic_arr.items():
        print(f"Clave: {llave}, Valor: {valor}")


imprimir_datos("Carlos", "Martín", "Herrera", Calle="10 de mayo")
print()
imprimir_datos("Arturo", "Becerril", "Herrera", telefono=12653627, calle= "San pablo")


class OperacionesMatematicas:
    def sumar(self, *arg):
        if len(arg) == 0:
            return 0
        elif len(arg) == 1:
            return arg[0]
        else:
            return sum(arg)
        
    def multiplicar(self, *arg):
        if len(arg) == 0:
            return 0
        elif len(arg) == 1:
            return arg[0]
        else:
            resultado = 1
            for ar in arg:
                resultado = resultado * ar
            return resultado
        

    def operaciones_complejas(self, operacion, *arg):
        if operacion == "sumar":
            return self.sumar(*arg)
        elif operacion == "multiplicar":
            return self.multiplicar(*arg)

op = OperacionesMatematicas()
print(op.operaciones_complejas("sumar"))
print(op.operaciones_complejas("sumar",2,45,7,8,10))
print(op.operaciones_complejas("multiplicar",1,2))
print(op.operaciones_complejas("multiplicar",1,2,25))


from multipledispatch import dispatch

#En esta clase se implementa la sobre carga de metodos
#Se basa a trabajar en la misma clase, con nombres de metodos iguales pero con diferente comportamiento
class Operaciones:

    #Trabajando con decoradores
    @dispatch(int, int)
    def suma(self, a, b):
        return a + b
    
    #Trabajando con decoradores
    @dispatch(int, int, int)
    def suma(self, a, b, c):
        return a - b- c


op = Operaciones()
print(op.suma(1,6))
print(op.suma(1,6,450))
"""
#En esta clase se aplica la sobre escritura
#Trabaja bajo la herencia, heredando los mismo metodos pero con comportamientos propios de la hija
class Vehiculo:
    def conducir(self, velocidad, a, b):
        print(f"El VEHICULO esta en movimiento a {velocidad} k/h", a+b)

#Heredando de la clase Vehiculo (padre) cambiamos el comportamiento 
#del metodo conducir
class Auto(Vehiculo):
    def conducir(self,marca):
        print(f"El AUTOMOVIL esta en movimiento de la marca {marca}")

vehi = Vehiculo()
auto = Auto()

vehi.conducir(180, 1, 5)

auto.conducir("mazda")












