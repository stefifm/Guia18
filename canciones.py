# Desarrollar un programa que permita administrar la información  de una
# aplicación de música por streaming.
#
# La información se debe almacenar en un vector de n registros  (n se
# ingresa por teclado), donde cada elemento representa una canción, con la
# siguiente información: título, duración (entre 1 y 15 minutos inclusive),
# cantidad de reproducciones, cantidad de descargas.

# El programa debe contar con un menú que implemente las siguientes opciones:
#
# Cargar n canciones de forma manual
# Cargar n canciones de forma automática
# Mostrar un listado de las canciones existentes, ordenado alfabéticamente por título.
# Determinar cuántas canciones existen para cada duración.  Mostrar los
# resultados.
# Buscar una canción cuyo título se ingresa por teclado. Si  existe,
# incrementar en 1 su cantidad de descargas y mostrar la  información
# actualizada. Si no existe, mostrar un aviso.
# Determinar cuántas canciones superan las 100 descargas,  y qué porcentaje
# representan sobre el total de canciones.
# Mostrar qué canción tiene mayor cantidad de reproducciones,
# y qué diferencia hay con su cantidad de descargas (sabiendo  que siempre
# existen más reproducciones que descargas).


import funcion_canciones

print("Programa principal")


def principal():
    n = funcion_canciones.validar(0)
    cancion = [None] * n


    opcion = 0
    print("Menú de opciones...")
    print("1. Carga de registros de forma manual")
    print("2. Carga de registros de forma automática")
    print("3. Listado ordenado de canciones")
    print("4. Canciones y su duración")
    print("5. Búsqueda de un título")
    print("6. Canciones que superan las 100 descargas y porcentaje")
    print("7. Mayor reproducción y diferencia con descargas")
    print("8. Salir")
    while opcion != 8:
        opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            funcion_canciones.opcion1(cancion)
        elif opcion == 2:
            funcion_canciones.opcion2(cancion)
        elif opcion == 3:
            funcion_canciones.opcion3(cancion)
        elif opcion == 4:
            funcion_canciones.opcion4(cancion)
        elif opcion == 5:
            funcion_canciones.opcion5(cancion)
        elif opcion == 6:
            funcion_canciones.opcion6(cancion)
        elif opcion == 7:
            funcion_canciones.opcion7(cancion)
        else:
            print("-------------Programa Finalizado-------------")



if __name__ == "__main__":
    principal()
