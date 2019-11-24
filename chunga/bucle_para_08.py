# Algoritmo para el ingreso de una clave de wifi si llega a tres veces ingresadas se detiene el programa
import os
i=0
while i<5:
    i=i+1
    b=os.sys.argv[1]
    if b!="Angel34#":
        print(" ERROR,clave incorrecta")
    else:
        print("clave correcta")
    if    i==3:
        break

print("lo sentimos parece que ingreso muchas veces una clave incorrectamente")
