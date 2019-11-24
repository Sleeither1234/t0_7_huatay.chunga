# Algoritmo para determinar el estado de una persona con hemorragia
import  os
total_de_sangre=float(os.sys.argv[1])
sangre_perdida=float(os.sys.argv[2])
porcentaje_de_sangre=((total_de_sangre-sangre_perdida)/total_de_sangre)*100
cont=0
while (cont<1):
    cont=cont+1
    if porcentaje_de_sangre>=75:
        print("el porcentaje es "+str(porcentaje_de_sangre))
        print("el paciente tiene mas posibilidades de vivir")

    else:
          print("el porcentaje es " + str(porcentaje_de_sangre))
          print("lo sentimos,parece que el paciente fallecera por falta de sangre")

