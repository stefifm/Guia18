#Definición del tipo registro Empleado

class Empleado:
    pass

#implementación 1 con funciones
#cargar el registro

def inicial(legajo, nombre, sueldo):
    empleado = Empleado()
    empleado.legajo = legajo
    empleado.nombre = nombre
    empleado.sueldo = sueldo
    return empleado
#aquí si hay que retornar el empleado


# Generar una cadena con los valores del registro
def to_string(empleado):
    resultado = " "
    resultado += "El empleado es: "
    resultado += "Legajo: " + str(empleado.legajo)
    resultado += " - Nombre: " + empleado.nombre
    resultado += " - Sueldo: " + str(empleado.sueldo)
    return resultado

#prueba
e1 = inicial(1, "Stefania", 350)
e2 = inicial(2, "Juan", 250)

print(to_string(e1))
print(to_string(e2))