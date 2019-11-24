#tabla de multiplicar

import os
#Asignacion de valores
numero=int(os.sys.argv[1])
valor=range(1,13)
#bucle para
for elemento in valor:
    producto=numero*elemento
    print(numero,"x",elemento,"=",producto)
#fin_for
print("fin del bubcle")
