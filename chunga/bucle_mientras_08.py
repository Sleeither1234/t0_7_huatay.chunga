# Algoritmo para determinar el acierto de los tiros de un basquebolista midiendo su capcaidad
import os
#asignacion de valores
distancia_desde_donde_lanza=int(os.sys.argv[1])
numero_de_tiros=0
#funcion para
while(numero_de_tiros<10):
    numero_de_tiros=numero_de_tiros+1
    if distancia_desde_donde_lanza<3:
           print("parece que entrara limpiamente el balon")
           distancia_desde_donde_lanza=int(input(print("ingresa la distancia en metros  desde donde lanza el jugador:")))
    elif distancia_desde_donde_lanza==3:
           print("parece que rebotara con el tablero pero entrara a la canasta")
           distancia_desde_donde_lanza=int(input(print("ingresa la distancia en metros  desde donde lanza el jugador:")))
    elif distancia_desde_donde_lanza>=4:
                        print("parece que fallara el tiro")
                        distancia_desde_donde_lanza=int(input(print("ingresa la distancia en metros  desde donde lanza el jugador:")))
    if(numero_de_tiros==10):
                print("programa terminado")


