#Definición del tipo registro Empleado

class Empleado:
    pass

#implementación 1 con funciones
#cargar el registro

def inicial(empleado, legajo, nombre, sueldo):
    empleado.legajo = legajo
    empleado.nombre = nombre
    empleado.sueldo = sueldo
#No hace falta retorno porque ya está hecho el registro


#Otra función para mostrar el registro
def mostrar(empleado):
    print("El empleado es:", empleado.legajo, "-", empleado.nombre, "-",
          empleado.sueldo)

e1 = Empleado()
e2 = Empleado()

inicial(e1, 1, "Stefania", 350)
inicial(e2, 2, "Juan",250)

mostrar(e1)
mostrar(e2)