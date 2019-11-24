# Votos Alianza y Universitario
import os
# Asignacion de valores
votos_alianza=0
votos_universitario=0
comando=0

# bucle mientras
while comando!="SALIR":
    comando=os.sys.argv[1]
    if comando=="A":
        votos_alianza=votos_alianza+1
        comando=input("ingrese los votos")
    elif comando=="U":
        votos_universitario=votos_universitario+1
        comando=input("ingrese los votos")
    #fin_si

#fin_mientras


# Se imprime comentarios
print("fin del bucle")
print("Los votos a universitario son: "+str(votos_universitario))
print("Los votos a Alianza son: "+str(votos_alianza))

#condicion if else
if votos_universitario>votos_alianza:
    print("el ganador es Universitario")
else:
    print("el ganador es Alianza")


print("Fin del bucle")#se imprime un comentario
