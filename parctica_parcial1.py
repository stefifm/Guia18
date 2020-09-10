# 2. Analizando Temperaturas
# El Servicio Metereológico Nacional solicitó un programa que mediante un
# menu de opciones, permita analizar las amplitudes térmicas desde
# diferentes  puntos de vista, para ello las opciones a las que el programa
# debe responder son:
#
# Cargar n analisis térmicos (n ingresado por el usuario), cuyos datos son:
# región, mes (numero del 1 al 12), temperatura máxima, temperatura mínima.
# Permitir informar la temperatura máxima promedio en el primer semestre
# Permitir informar la región y el mes en que se registró la menor mínima
# del año
# Salir


import funciones_practica1


def principal():
    #Presentación del vector térmico
    n = funciones_practica1.validar(0)
    termico = [None] * n

    opcion = 0
    print("Menú de opciones")
    print("1. Cargar el análisis térmico")
    print("2. Informar la temperatura máxima promedio del primer semestre")
    print("3. Informar la región y mes de la menor mínima del año")
    print("4. Salir")
    while opcion != 4:

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            funciones_practica1.opcion1(termico)
        elif opcion == 2:
            funciones_practica1.opcion2(termico)
        elif opcion == 3:
            funciones_practica1.opcion3(termico)
        else:
            print("-------------Programa finalizado-----------")


if __name__ == "__main__":
    principal()