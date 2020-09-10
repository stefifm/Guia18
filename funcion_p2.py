import random

print("Funciones para la práctica de parcial 2")

class Cartas:
    def __init__(self, part1, part2, palo1, palo2, num1, num2):
        self.participante1 = part1
        self.participante2 = part2
        self.palo1 = palo1
        self.palo2 = palo2
        self.numero1 = num1
        self.numero2 = num2

def cargar_vector(jugadores):
    palo = ("oros", "copas", "espadas", "bastos")
    for i in range(len(jugadores)):
        participante1 = input("Ingrese el nombre del primer jugador: ")
        participante2 = input("Ingrese el nombre del segundo jugador: ")
        palo1 = random.choice(palo)
        palo2 = random.choice(palo)
        numero1 = random.randint(1, 12)
        numero2 = random.randint(1, 12)
        j = Cartas(participante1, participante2, palo1, palo2, numero1, numero2)
        jugadores[i] = j
    return jugadores

def ronda(jugadores):
    n = len(jugadores)
    for i in range(n):
        if jugadores[i].numero1 > jugadores[i].numero2:
            id_ganador = jugadores[i].participante1
        elif jugadores[i].numero2 > jugadores[i].numero1:
            id_ganador = jugadores[i].participante2
        elif jugadores[i].numero1 == jugadores[i].numero2:
            if jugadores[i].palo1 == "oros":
                id_ganador = jugadores[i].participante1
            else:
                if jugadores[i].palo2 == "oros":
                    id_ganador = jugadores[i].participante2
        return id_ganador

def ganador(r1, r2, r3):
    acu1 = r1.numero1 + r2.numero1 + r3.numero1
    acu2 = r1.numero2 + r2.numero2 + r3.numero2
    return acu1, acu2
