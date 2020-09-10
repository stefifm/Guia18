import random


class Cartas:
    def __init__(self, part, palo):
        self.jugador = part
        self.palo = palo
        self.numero = random.randint(1, 12)

def to_string(cartas):
    resultado = " "
    resultado += "El jugador es: "
    resultado += "Nombre: " + cartas.jugador
    resultado += "Palo de la carta: " + str(cartas.palo)
    resultado += "Valor de la carta: " + str(cartas.numero)
    return resultado

def ronda(j1, j2):
    if j1.numero > j2.numero:
        id_ganador = j1.jugador
    elif j2.numero > j1.numero:
        id_ganador = j2.jugador
    else:
        if j1.palo == "oros":
            id_ganador = j1.jugador
        else:
            id_ganador = j2.jugador
    return id_ganador




print("Práctica de parcial 2")

def princpal():
    print("Juego de cartas de la baraja española")
    pal = ("oros", "copas", "espadas", "bastos")
    palo = random.choice(pal)
    nombre = input("Ingrese el nombre del primer jugador: ")
    jugador1 = Cartas(nombre, palo)
    to_string(jugador1)

    nombre = input("Ingrese el nombre del segundo jugador: ")
    jugador2 = Cartas(nombre, palo)
    to_string(jugador2)

    print("Primera ronda")
    ronda1 = ronda(jugador1, jugador2)
    print("Ganador de la primera ronda:", ronda1)
    print("Segunda ronda")
    ronda2 = ronda(jugador1, jugador2)
    print("Ganador de la segunda ronda:", ronda2)
    print("Tercera ronda")
    ronda3 = ronda(jugador1, jugador2)
    print("Ganador de la tercera ronda:", ronda3)








if __name__ == '__main__':
    princpal()