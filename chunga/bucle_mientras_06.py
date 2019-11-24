# Algoritjmo para mostrar numeros cuadrados menores que 64
import  os
i=int(os.sys.argv[1])
while(i**2<=64):
    print("los numero cuadrados menores e iguales que 64 son",i**2)
    i=i+1
if i>=9:
    print("parece que ingreso un numero invalido")

print("programa terminado")

