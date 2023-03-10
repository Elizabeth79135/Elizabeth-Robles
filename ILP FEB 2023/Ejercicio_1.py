
# CALCULAR EL PROMEDIO DE 3 CALIFICACIONES Y DECIR SI ES "APROBADO" O "REPROBADO"

# ENTRADA DE DATOS
calificacion_1 = float(input("Calificación 1: "))
calificacion_2 = float(input("Calificación 2: "))
calificacion_3 = float(input("Calificación 3: "))

#PROCESO
suma= calificacion_1 + calificacion_2 + calificacion_3
promedio= suma / 3

  
#SALIDA DE DATOS
print("El promedio es =",round(promedio,2))


if (promedio>=7 and promedio<10):
    print("APROBADO")
elif (promedio>=6 and promedio<7) :
    print("DE PANSASO")
elif (promedio>0 and promedio<6):
    print("REPROBADO")
elif (promedio<0 or promedio>10) :
    print ("PROMEDIO INVÁLIDO")