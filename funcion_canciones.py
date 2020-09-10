import random

print("Funciones para canciones")

class Cancion:
    def __init__(self, titulo, long, repro, down):
        self.titulo = titulo
        self.duracion = long
        self.reproduccion = repro
        self.descargas = down


def to_string(cancion):
    r = " "
    r += "El nombre de la canción: " + cancion.titulo
    r += "- Duración: " + str(cancion.duracion)
    r += "- Cantidad de reproduccion: " + str(cancion.reproduccion)
    r += "- Cantidad de descargas: " + str(cancion.descargas)
    r += "\n"
    return r

#Opcion 1: carga manual


def validar_rango(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input("Ingrese un valor entre " + str(inf) +
                          " y " + str(sup) + ": "))
        if n < inf or n > sup:
            print("Error")
    return n

def validar(inf):
    n = inf
    while n <= inf:
        n = int(input("Cargue el tamaño del vector: "))
        if n <= inf:
            print("Error. Ingrese un número que sea diferente a cero.")
    return n


def carga_manual(cancion):
    for i in range(len(cancion)):
        titulo = input("Ingrese el nombre de la canción: ")
        duracion = validar_rango(1, 15)
        reproduccion = int(input("Ingrese la cantidad de reproducciones: "))
        descargas = int(input("Ingrese la cantidad de descargas: "))

        c = Cancion(titulo, duracion, reproduccion, descargas)
        cancion[i] = c
    return cancion

def opcion1(cancion):
    print("Cargue los datos de la canción")
    carga_manual(cancion)

#opcion 2: carga automática

def carga_automatica(cancion):
    titulos = (
    'CANCIÓN DE TÍTERES', 'CANCIÓN DEL JACARANDÁ', 'CANCIÓN DE LA VACUNA',
    'EL SHOW DEL PERRO SALCHICHA', 'LA MONA JACINTA',
    'LA VACA ESTUDIOSA', 'TWIST DEL MONO LISO', 'MARCHA DE OSÍAS',
    'MANUELITA, LA TORTUGA', 'CANCIÓN PARA VESTIRSE',
    'EL REINO DEL REVÉS', 'CANCIÓN DE TOMAR EL TÉ',
    'LA CALLE DEL GATO QUE PESCA', 'DON DOLÓN DOLÓN', 'CANCIÓN DEL JARDINERO',
    'JUGAR X JUGAR', 'SACO UNA MANITO', 'MANOS DIVERTIDAS', 'YO NUNCA VÍ',
    'TIMOTEO', 'YO TENGO UNA CASITA', 'HABÍA UNA VEZ UN AVIÓN',
    'LA SEÑORA CUCARACHA', 'CINCO RATONCITOS', 'EL TALLARÍN',
    'MAMUT CHIQUITITO', 'EL COCODRILO', 'WINCI ARAÑA', 'LA VIBORITA',
    'CHOLITO', 'CUENTO DEL GUSANITO', 'HOCKY POCKY', 'CANTANDO CON ADRIANA',
    'PARA DORMIR A UN ELEFANTE', 'MICHU MICHU',
    'EL POLLITO LITO', 'RONDA DE LOS CONEJOS', 'A MIS MANOS',
    'FAMILIA DE DEDOS', 'ABRO UNA MANO', 'DICEN QUE LOS MONOS',
    'ESTE PECECITO', 'UN SUEÑO LINDO', 'ESTA ES MI CASA', 'EL CALIPSO',
    'EL ZOOLÓGICO', 'LA PATITA LULÚ',
    'DICEN QUE DICEN', 'HIPOROPOPÓ', 'ESTATUA', 'BAILANDO EL BUGUI BUGUI',
    'CENA EN EL ZOO', 'EL BAILE DEL COCODRILO',
    'ROCO EL HURÓN', 'SUPER DISCO CHINO', 'LOS MONOS Y LAS MONAS',
    'HOLA Y ADIÓS')
    for i in range(len(cancion)):
        titulo = random.choice(titulos)
        duracion = random.randint(1, 15)
        reproduccion = random.randint(10, 500)
        descargas = random.randint(10, 500)
        c = Cancion(titulo, duracion, reproduccion, descargas)
        cancion[i] = c
    return cancion

def opcion2(cancion):
    print("Presione Enter para cargar el vector...")
    input()
    carga_automatica(cancion)
    print("Hecho, ya realizó la carga")

#opcion 3
#Función orden_sort para ordenar de menor a mayor
#algoritmo de selección directa
def orden_sort(cancion):
    n = len((cancion))
    for i in range(n-1):
        for j in range(i+1,n):
            if cancion[i].titulo > cancion[j].titulo:
                cancion[i], cancion[j] = cancion[j], cancion[i]
#mostrar el arreglo ordenado
def display(cancion):
    for i in range(len(cancion)):
        print(to_string(cancion[i]))

#armado de la opcion 3 con el arreglo ordenado y su muestra
def opcion3(cancion):
    if cancion[0] == None:
        print("No se han cargado los datos")
        return

    print("Lista de canciones en orden alfabético")
    orden_sort(cancion)
    display(cancion)

#opcion4
#Aquí usar un vector de registro de conteo
def contar(cancion):
    count_duracion = [0] * 15
    for i in range(len(cancion)):
        d = int(cancion[i].duracion)-1
        count_duracion[d] += 1
    for i in range(15):
        if count_duracion[i] != 0:
            print("Cancion:",i+1,"min","Duración:",count_duracion[i])

def opcion4(cancion):
    if cancion[0] is None:
        print("No hay datos cargados en el arreglo")
        return
    contar(cancion)


#opcion5
#hacer una busqueda de si se encuentra el título
def buscar(cancion, nom):
    for i in range(len(cancion)):
        if cancion[i].titulo == nom:
            return i
    return -1

def opcion5(cancion):
    if cancion[0] is None:
        print("No hay datos cargados en el arreglo")
        return
    #variable nom para buscar el título de la canción
    #seguido por una variable pos donde se activa la funcion de busqueda
    nom = input("Ingrese el título de la canción a buscar: ")
    pos = buscar(cancion, nom)
    #si pos es distinto a -1, es decir, si está el valor
    if pos != -1:
        #sumarle 1 a la descargas de la cancion encontrada
        #y luego se muestra
        cancion[pos].descargas += 1
        print("Canción encontrada. Se incrementa en 1 su cantidad de "
              "descarga")
        print("Datos modificados de la canción encontrada:")
        print(to_string(cancion[pos]))
    else:
        #Mostrar en caso de que no se encuentre el título buscado
        print("No se pudo encontrar esa canción")

#opcion6

def mas_de_100(cancion):
    contador = 0
    for i in range(len(cancion)):
        if cancion[i].descargas > 100:
            contador += 1
    porcentaje = round(contador * 100 / len(cancion), 2)
    print("Cantidad de canciones que superan las 100 descargas:",contador,
          "y representa el",porcentaje,"%","sobre el total")

def opcion6(cancion):
    if cancion[0] is None:
        print("No hay datos cargados en el arreglo")
        return
    mas_de_100(cancion)

#opcion7
def mayor_reproduccion(cancion):
    mayor = cancion[0]
    for i in range(len(cancion)):
        if cancion[i].reproduccion > mayor.reproduccion:
            mayor = cancion[i]
    return mayor

def opcion7(cancion):
    mayor = mayor_reproduccion(cancion)
    diferencia = mayor.reproduccion - mayor.descargas
    print("La canción con mayor reproduccion:",mayor.titulo,"y hay una "
                                                            "diferencia de",
          diferencia,"respecto a la cantidad de descargas")