# votar correctamente la basura segun la cantidad de basura en un recipiente
import  os
#asignacion de valores
i=0
#fin_para
while i<3:
    i=i+1
    capacidad=int(os.sys.argv[1])
    basura=int(os.sys.argv[2])
    if basura==capacidad:
        print("votar el recipiente")
    elif basura<capacidad:
        print("El recipiente aun no esta lleno")
    elif basura==0:
        print("el recipiente esta vacio")
    else:
        print("ERROR! , parece que la basura excede ala capacidad, por favor ingrese un numero menor o igual a la capacidad")


#se imprime un comentarioo
print("Fin del bucle ")
