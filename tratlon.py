# 1. Triatlon
# El Comité Argentnio de Atletismo llevo a cabo una prueba atletica  de
# Triatlón, nos solicito un programa que valide lo anotado por los jueces
# del evento, para dicho propósito se deben cargar los datos de los tres
# atletas con mejor promedio. De cada atleta se conocen Nombre,  Tiempo
# Natacion, Tiempo Ciclismo, Tiempo Corriendo (todo en minutos  para
#  simplificar los calculos).
#
# Usted debe:
#
# Informar tiempo promedio de cada competidor
# Determinar el podio, indicando el nombre del primer, segundo y tercer
# mejor promedio

import random

print("Triatlón")

class Atletas:
    def __init__(self, nom):
        self.nombre = nom
        self.natacion = random.randint(10, 30)
        self.ciclismo = random.randint(10, 40)
        self.corriendo = random.randint(10, 60)

def to_string(atletas):
    resultado = " "
    resultado += "El atleta es: "
    resultado += "Nombre: " + atletas.nombre
    resultado += "Tiempo natación: " + str(atletas.natacion)
    resultado += "Tiempo ciclismo: " + str(atletas.ciclismo)
    resultado += "Tiempo corriendo: " + str(atletas.corriendo)
    return resultado

def promedio_tiempos(atletas):
    suma = atletas.ciclismo + atletas.natacion + atletas.corriendo
    promedio = round(suma / 3, 2)
    return promedio

def podio(nom1, prom1, nom2, prom2, nom3, prom3):
    if prom1 < prom2 and prom1 < prom3:
        primero = prom1
        id_primero = nom1
        if prom2 < prom3:
            segundo = prom2
            id_segundo = nom2
            tercero = prom3
            id_tercero = nom3
        else:
            segundo = prom3
            id_segundo = nom3
            tercero = prom2
            id_tercero = prom2
    elif prom2 < prom3:
        primero = prom2
        id_primero = nom2
        if prom1 < prom3:
            segundo = prom1
            id_segundo = nom1
            tercero = prom3
            id_tercero = nom3
        else:
            segundo = prom3
            id_segundo = nom3
            tercero = prom1
            id_tercero = prom1
    else:
        primero = prom3
        id_primero = nom3
        if prom1 < prom2:
            segundo = prom1
            id_segundo = nom1
            tercero = prom2
            id_tercero = nom2
        else:
            segundo = prom2
            id_segundo = nom2
            tercero = prom1
            id_tercero = nom1
    return id_primero, id_segundo, id_tercero


def test():
    nombre = input("Ingrese el nombre del atleta 1: ")
    atleta1 = Atletas(nombre)
    to_string(atleta1)

    nombre = input("Ingrese el nombre del atleta 2: ")
    atleta2 = Atletas(nombre)
    to_string(atleta2)

    nombre = input("Ingrese el nombre del atleta 3: ")
    atleta3 = Atletas(nombre)
    to_string(atleta3)

    prom1 = promedio_tiempos(atleta1)
    prom2 = promedio_tiempos(atleta2)
    prom3 = promedio_tiempos(atleta3)

    print("Promedio de",atleta1.nombre,":",prom1)
    print("Promedio de", atleta2.nombre,":", prom2)
    print("Promedio de", atleta3.nombre,":", prom3)

    pri, seg, ter = podio(atleta1.nombre, prom1, atleta2.nombre, prom2,
                          atleta3.nombre, prom3)
    print("El primero:",pri)
    print("Segundo:",seg)
    print("Tercero:",ter)

if __name__ == "__main__":
    test()