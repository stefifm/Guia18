#Crear el tipo de registro Alumno
class Alumno:
    def __init__(self, legajo, nombre, promedio):
        self.legajo = legajo
        self.nombre = nombre
        self.promedio = promedio

# Hacer una función para mostrar o armar cadena con los datos del registro
def to_string(alumno):
    resultado = " "
    resultado += "El alumno es: "
    resultado += "Legajo: " + str(alumno.legajo)
    resultado += " - Nombre: " + alumno.nombre
    resultado += " - Sueldo: " + str(alumno.promedio)
    return resultado

#funciones propias

def cargar_vector(v):
    for i in range(len(v)):
        #cargar datos del alumno
        legajo = int(input("Ingrese el legajo: "))
        nombre = input("Ingrese el nombre: ")
        promedio = float(input("Ingrese el promedio: "))
        #crear el alumno
        a = Alumno(legajo, nombre, promedio)
        #grabar en el vector
        v[i] = a
    return v

def mostrar_vector(v):
    for i in range(len(v)):
        #muestra cada alumno invocando a la función to_string
        print(to_string(v[i]))

def mostrar_prom_mas_8(v):
    #recorrer el vector
    print("Alumnos con promedio mayor a 8: ")
    for i in range(len(v)):
        if v[i].promedio > 8:
            print(to_string(v[i]))

def ordenar(vec):
    #Crea una copia del vector y ordena la copia, dejando el vector original
    # sin orden
    vec_orden = vec[:]
    n = len(vec)
    for i in range(n-1):
        for j in range(i+1, n):
            aux = vec_orden[i]
            vec_orden[i] = vec_orden[j]
            vec_orden[j] = aux
    return vec_orden

def contar_notas(vec):
    vc = 10 * [0]
    for i in range(vec):
        k = int(vec[i].promedio) - 1
        vc[k] += 1
    return vc


# Función principal
def test():
    #pedir la cantidad de alumnos
    n = int(input("Ingrese la cantidad de alumnos: "))
    #crear el vector de alumnos
    v = n * [None]
    #cargar los alumnos
    cargar_vector(v)
    #mostrar los alumnos
    mostrar_vector(v)
    #promedio mayor a 8
    mostrar_prom_mas_8(v)
    #Mostrar el vector ordenado
    vector_ordenado = ordenar(v)
    mostrar_vector(vector_ordenado)
    #Mostrar el vector de conteo
    vec_conteo = contar_notas((vector_ordenado))
    mostrar_vector(vec_conteo)



if __name__ == "__main__":
    test()