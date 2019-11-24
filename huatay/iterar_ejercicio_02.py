#La tabla de multiplicar de un numero
import  os
tabla=(1,2,3,4,5,6,7,8,9,10) #asignacion de los valores del 1 al 10 a la siguientes  variable tabla
multiplicar=int(os.sys.argv[1]) #asignacion del valor 5 a la variable multiplicar
for numero in tabla: #funcion iterarador,para cada numero se multiplica la variable multiplicar
#fin_iterar
    print(multiplicar, "x", numero,"=",multiplicar*numero) #imprime los valores de la variable multiplicar por numero

