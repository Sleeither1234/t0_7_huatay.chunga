# Determinacion si peleares por una vacante segun tu puntaje obtenido de tres estudiantes
import os
i=0
while i<3:
    i=i+1
    ptje_obtenido=float(os.sys.argv[1])
    ptje_minimo=31.5
    if ptje_obtenido<31.5 :
        print("lo sentimos no podras pelear por una vacante ya que no pasaste el puntaje minimo")
    elif ptje_obtenido==59.5:
         print("EXCELENTE,FELICIDADES has obtenido el puntaje maximo del examen ")
    else:
        print("felicidades,podras competir por una vacante para tu ingreso,sigue esforzandote para el siguiente examen")