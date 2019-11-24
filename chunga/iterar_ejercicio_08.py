#impresion numeros impares
import os

#asignacion de las variables
numeros=(1,3,5,7,9,11)
multiplicar=int(os.sys.argv[1])

#funcion iterar
for numero_impar in numeros:
    print(numero_impar*multiplicar)
#fin_iterar

#se imprime un pequeño comentario
print("Fin del bucle")
