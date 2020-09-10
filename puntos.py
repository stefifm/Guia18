import random


n = 16
vector = [None] * n

nom = ("Mercedes", "Red Bull", "Ferrari", "McLaren", "Williams",
           "Racing Point", "Renault", "Alpha Tauri", "Haas", "Alfa Romeo",
           "Team Penske", "Toyota Gazoo Racing", "Peugeot Sport Team",
           "Chip Ganassi Racing", "RLL Racing", "Action Express")

for i in range(len(vector)):
    nombre1 = random.choice(nom)
    puntos1 = random.randint(100, 700)
    nombre2 = random.choice(nom)
    puntos2 = random.randint(100, 700)
    vector  = nombre1, puntos1, nombre2, puntos2

mayor = [None] * 8
for i in range(len(mayor)):
    pass



