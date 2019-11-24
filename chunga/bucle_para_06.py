# que hacer segun el color de los semaforos
import  os
#asignacion de valores
i=0
#funcion para
while i<3:
    i=i+1
    a=os.sys.argv[1]
    if a=="rojo":
        print("alto!,el semaforo esta en rojo")
    elif a=="amarillo":
        print("por favor,encienda motores para acelerar")
    elif a=="verde":
        print("no se se detenga,siga acelerandot")
    elif a!="rojo,verde,amarillo":
        print("parece que ingreso un color invalido,")
#fin_para
# se imprime un comentario
print("Fin del bucle")



