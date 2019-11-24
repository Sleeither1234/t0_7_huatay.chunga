# impresion de los valoores del 1 al 10 y su suma de los dos valores anteriores
import os
total=int(os.sys.argv[1]) #asignacion del valor 0 a la variable total
for numero in range(0,10): #funcion iterar_rango,ingresa numero hasta que el rango se agote
    total=total+numero  #asginacion del valor total
    print(numero) #se imprime el valor del numero y la suma total de los numeros anteriores
    print("el total es: "+str(total))
print("Fin del bucle")#se imprime un comentario
