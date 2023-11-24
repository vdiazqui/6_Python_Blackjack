import random
import time

# Es un diccionario llamado "Cartas" que contiene el codigo de unicode (para que salga el dibujo) de cada carta de la baraja 
cartas = { 
    chr(0x1f0a1): 11,
    chr(0x1f0b1): 11,
    chr(0x1f0c1): 11,
    chr(0x1f0d1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0b2): 2,
    chr(0x1f0c2): 2,
    chr(0x1f0d2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0b3): 3, 
    chr(0x1f0c3): 3, 
    chr(0x1f0d3): 3, 
    chr(0x1f0a4): 4,
    chr(0x1f0b4): 4, 
    chr(0x1f0c4): 4, 
    chr(0x1f0d4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0b5): 5, 
    chr(0x1f0c5): 5,
    chr(0x1f0d5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0b6): 6, 
    chr(0x1f0c6): 6, 
    chr(0x1f0d6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0b7): 7, 
    chr(0x1f0c7): 7, 
    chr(0x1f0d7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0b8): 8, 
    chr(0x1f0c8): 8, 
    chr(0x1f0d8): 8, 
    chr(0x1f0a0): 9, 
    chr(0x1f0b9): 9,
    chr(0x1f0c9): 9, 
    chr(0x1f0d9): 9, 
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10, 
    chr(0x1f0ba): 10, 
    chr(0x1f0bb): 10,
    chr(0x1f0bd): 10, 
    chr(0x1f0be): 10, 
    chr(0x1f0ca): 10,
    chr(0x1f0cb): 10,
    chr(0x1f0cd): 10,
    chr(0x1f0ce): 10,
    chr(0x1f0da): 10,
    chr(0x1f0db): 10,
    chr(0x1f0dd): 10,
    chr(0x1f0de): 10, 
} 

# Es una lista con las claves del diccionario creado justo antes
lista = list(cartas.keys())

# Turno del jugador, primero se le reparten dos cartas las cuales se imprimen y mas tarde se imprime su puntuacion
print("TURNO DEL JUGADOR")

carta_1_jugador = random.choice(lista)
time.sleep(0.5)
print("Carta del jugador: "+carta_1_jugador)
carta_2_jugador = random.choice(lista)
time.sleep(0.5)
print("Carta del jugador: "+carta_2_jugador)

time.sleep(1)
puntuacion_jugador = cartas[carta_1_jugador] + cartas[carta_2_jugador]
print("La puntuacion del jugador es: "+str(puntuacion_jugador))
diferencia_jugador = 21 - puntuacion_jugador

# Bucle que tiene lugar cuando la puntuacion del jugador sea menor a 21, y le pregunta si quiere otra carta
while puntuacion_jugador < 21:
    time.sleep(0.5)
    pregunta = input("Quieres otra carta? Si (y)/ No (n): ")
    if pregunta == "y": 
        carta_jugador = random.choice(lista)
        print("Carta del jugador: "+carta_jugador)
        puntuacion_jugador += cartas[carta_jugador]
        diferencia_jugador = 21 - puntuacion_jugador
        print("La puntuacion del jugador es: "+str(puntuacion_jugador))
        if diferencia_jugador < 0:
            break
    elif pregunta == "n":
        break


carta_1_banca = random.choice(lista)
carta_2_banca = random.choice(lista)
puntuacion_banca = cartas[carta_1_banca] + cartas[carta_2_banca]

# Bucle que se da cuando el jugador no se ha pasado por lo que es el turno de la banca
if diferencia_jugador >=0: 
    print()
    time.sleep(1)
    print("TURNO DE LA BANCA")
    time.sleep(0.5)
    print("Carta de la banca: "+carta_1_banca)
    time.sleep(0.5)
    print("Carta de la banca: "+carta_2_banca)
    time.sleep(0.5)
    print("La puntuacion de la banca es: "+str(puntuacion_banca))
    # Otro bucle para que la banca reciba carta si tiene menos de 17 puntos o se plante si tiene 17 o más (normas blackjack)
    while True: 
        if puntuacion_banca <17:
            carta_banca = random.choice(lista)
            time.sleep(0.5)
            print("Carta de la banca: "+carta_banca)
            puntuacion_banca += cartas[carta_banca]
            diferencia_banca = 21 - puntuacion_banca
            print("La puntuacion de la banca es: "+str(puntuacion_banca))
        elif 17 <= puntuacion_banca <= 21:
            time.sleep(0.5)
            print("La banca se planta.")
            break
        else:
            time.sleep(0.5)
            print("La banca se ha pasado.")
            break

diferencia_banca = 21 - puntuacion_banca

# Asignacion de quien gana, pierde o si empatan
time.sleep(1)
if diferencia_jugador == 0:
    print("Muy bien! Has hecho Blackjack.")
if puntuacion_banca > 21:
    print("Muy bien. Has ganado.")    
elif diferencia_jugador < 0:
    print("Has perdido. Te has pasado.")
elif diferencia_jugador > diferencia_banca:
    print("Has perdido. Te gana la banca.")
elif diferencia_jugador < diferencia_banca:
    print("Has ganado. Enhorabuena!")
else:
    print("Ni ganas ni pierdes. Habeis empatado.")