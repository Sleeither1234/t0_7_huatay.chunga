# Algoritmo para solucion determinar como son las raices cuadraticas
import os
print("la ecuacion genereal es A**2+Bx+C")
print("por favor A>0 ,ya que si no ,no seria ecuacion cuadratica si no lineal")
A=int(os.sys.argv[1])
B=int(os.sys.argv[2])
C=int(os.sys.argv[3])
discriminante=B**2-4*A*C
cont=0
while(A>=0 and cont<1):
    cont+=1
    if discriminante>0:
        print("el valor de la discriminante es:",discriminante)
        print("la ecuacion general tiene dos soluciones reales y diferentes")
    elif discriminante==0:
        print("el valor de la discriminante es:",discriminante)
        print("la ecuacion general tiene soluciones reales e iguales")
    else:
        print("el valor de la discriminante es:",discriminante)
        print("la ecuacion general tiene soluciones conplejas")

# Se imprime un comentario
print("Fin del bucle")
