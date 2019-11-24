# Pedir notas

import os
# Asignacion de valores
nota=int(os.sys.argv[1])

# Bucle mientras nota sea mayor a 100 o menor a o
while nota>100 or  nota<0:
    nota=int(input("ingrese la nota 1: "))
#fin_while

#se imprime una frase
print("fin del bucle")
