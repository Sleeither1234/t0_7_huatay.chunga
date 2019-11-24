import os
# Fecha de nacimiento

# Asignacion de valores
edad=int(os.sys.argv[1])
año_nacimiento=int(os.sys.argv[2])

# valor predeterminado
año_actual=int(os.sys.argv[3])

# Calculo
año1_actual=año_actual-edad
#bucle mientras
while año1_actual-año_nacimiento!=edad:
    print("año de nacimiento invalido")
    break
    año_nacimiento=int(os.sys.argv[2])
    edad=int(os.sys.argv[1])
    año_actual=int(os.sys.argv[3])
#fin_si

# se imprime un comentario
print("Fin del bucle")

