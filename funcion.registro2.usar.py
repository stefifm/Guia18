
#Definir el tipo de registro Empleado
class Empleado:
    def __init__(self, legajo, nombre, sueldo):
        self.legajo = legajo
        self.nombre = nombre
        self.sueldo = sueldo

# Generar una cadena con los valores del registro
def to_string(empleado):
    resultado = " "
    resultado += "El empleado es: "
    resultado += "Legajo: " + str(empleado.legajo)
    resultado += " - Nombre: " + empleado.nombre
    resultado += " - Sueldo: " + str(empleado.sueldo)
    return resultado

#test
e1 = Empleado(1, "Stefania", 450)
e2 = Empleado(2, "Juan", 250)

print(to_string(e1))
print(to_string(e2))