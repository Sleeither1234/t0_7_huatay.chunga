import os
# Pedir colores

# Asignacion de valores
color=int(int(os.sys.argv[1]))

# Bucle mientras el color sea diferente a 1 y a 2
while color!=1 and color!=2:
    print("color ingresado incorrecto")
    color=int(input("seleccione el color 1 o 2 "))

#fin_while

# Si el color es 1  o el color es 2

if color==1:
    print("el color elejido es blanco")
elif color==2:
    print("el color elejido es negro")

#fin_si

print("Fin del bucle")#se imprime un comentario