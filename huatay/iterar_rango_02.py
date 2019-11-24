#Tabla del numero 5
import os
multiplicar=int(os.sys.argv[1]) #asignacion del valor 5 a la variable multiplicar
for numero in range(0,16): #funcion iterarador en rango,para cada numero se multiplica la variable multiplicar
#fin_iterar_rango
    print(multiplicar, "x", numero,"=",multiplicar*numero) #imprime los valores de la variable multiplicar por numero

print("Fin del bucle")#se imprime un comentario