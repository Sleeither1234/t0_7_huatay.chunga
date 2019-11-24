# Suma de cuadrados
import os
i=int(os.sys.argv[1]) #se asigna el valor 0 para poder partir desde el principio
suma=int(os.sys.argv[2]) #se asigna el valor 0 par poder partir  desde el principio
while(i<=5): #se asigna la condicion a la variable i para que sea menor e igual a 5
    print(i**2) #se imprime los valores de la variable i al cuadrado
    suma=suma+(i**2) #se asigna el valor de la variable suma
    i=i+1 #se incrementa en 1 la variable 1 ya que si no es el caso se volvera un bucle infinito
#fin fo
print("esta es la suma total:",suma) #se imprime el valor de la suma total

print("Fin del bucle")#se imprime un comentario
