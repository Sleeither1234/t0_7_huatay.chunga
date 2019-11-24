# Determinacion del estado de salud de tres persona segun los kilogramos de su cuerpo
import os
i=0
while i<3:
    i+=1
    estatura=float((os.sys.argv[1]))
    peso=int(os.sys.argv[2])
    if estatura>1.80 and (peso>60 and peso<80):
        print("su salud esta en excelentes condiciones")
    elif peso>80 and peso<90:
        print("parece que esta subiendo de peso,cuide su alimentacion")
    elif peso<60:
        print("parece que padece de anemia,se debe deber a una mala alimentacion")
    else:
        print("usted tiene sobrepeso,eso podria afectar drsticamente a su salud")



print("Fin del bucle")#se imprime un comentario