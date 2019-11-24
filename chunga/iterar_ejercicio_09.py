#Multiplos de 5 menores que 70
import os

#asignacion de valores
valores=(1,2,3,4,5,6,7,8,9,10,11,12,13)
multiplos=int(os.sys.argv[1])

#funcion iterar
for variable in valores:
    print(variable*multiplos)
#fin_iterar

#se imprime un comentario
print("Fin del bucle")