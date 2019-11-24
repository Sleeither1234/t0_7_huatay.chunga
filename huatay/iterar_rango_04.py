# Multiplos de 3 menores de 60en forma creciente
import os
#asignacion de valores
multiplos=int(os.sys.argv[1])

#funcion iterar
for c in range (1,20):
#fin_iterar_rango
 print(c*multiplos)
 if c*multiplos>=80:
     print("valores desgastados")

print("Fin del bucle")#se imprime un comentario
