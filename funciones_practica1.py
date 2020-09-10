import random

print("Funciones para la practica 1 parcial")

class Termico:
    def __init__(self, reg, mes, max, min):
        self.region = reg
        self.mes = mes
        self.maxima = max
        self.minima = min


def to_string(termico):
    r = " "
    r += "Temperaturas a analizar...."
    r += "Region: " + str(termico.region)
    r += "- Mes: " + str(termico.mes)
    r += "- Temperatura máxima: " + str(termico.maxima)
    r += "- Temperatura mínima: " +str(termico.minima)
    return r



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
        n = int(input("Cargue la cantidad de temperaturas: "))
        if n <= inf:
            print("Error. Ingrese un número que no sea cero")
    return n

def read(termico):
    n = len(termico)
    for i in range(n):
        region = random.randint(0, 4)
        mes = random.randint(1, 12)
        maxima = random.randint(10, 40)
        minima = random.randint(1, 15)
        termico[i] = Termico(region, mes, maxima, minima)
    return termico

def opcion1(termico):
    print("Cargue los datos de las temperaturas")
    read(termico)

#Opcion 2
def rango_trimestre(semestre):
    if semestre == 1:
        return range(6)
    else:
        return range(6, 12)


def promedio_maxima_semestre(termico):
    semestre = validar_rango(1, 2)
    suma = 0
    rango = rango_trimestre(semestre)
    for i in rango:
        suma += termico[i].maxima
    promedio_max = round(suma / len(rango), 2)
    return semestre, promedio_max

def opcion2(termico):
    if termico[0] == None:
        print("No hay datos cargados")
        return
    semestre = promedio_maxima_semestre(termico)
    print("Promedio de temperatura maxima en el semestre",semestre[0],
          "fue de",semestre[1])

#Opcion 3
def minima_anual(termico):
    menor = termico[0]
    cant = len(termico)
    for i in range(cant):
        if termico[i].minima < menor.minima:
            menor = termico[i]
    return menor

def opcion3(termico):
    if termico[0] == None:
        print("No hay datos cargados")
        return
    menor = minima_anual(termico)
    print("Región:",menor.region,"Mes:",menor.mes,"fue la menor mínima anual "
                                                 "y es de:",menor.minima)