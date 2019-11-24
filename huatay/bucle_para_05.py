import os
i=0
while i<2:
    i+=1
    ataque_del_personaje=int(os.sys.argv[1])
    if ataque_del_personaje>80:
        print("en hora buena,mataras a la unidad")
        M="mele"
        R="rango"
        rpta=os.sys.argv[2]
        if rpta=="mele":
            print("usted recibira 40 de oro")
        elif rpta=="rango":
            print("usted recibira 37 de oro")
    else:
        print("uf fallaste,no recibiras oro ")


print("Fin del bucle")#se imprime un comentario