import os
i=0
microondas=100
while i<1:
    i=i+1
    ventana=float(os.sys.argv[1])
    sueldo=float((10*(ventana))/3)
    print("por cada ventana ñlimpiada gana 3 ventanas gana 10 dolares")
    print(sueldo)
if sueldo>100:

     print("podra comprarse el horno microondas")

elif (sueldo)<100:

    vuelto=microondas-sueldo
    print("aun le falta "+ str(round(vuelto))+" para la compra dl microndas")


#se escribe un comentario
print("Fin del bucle")
