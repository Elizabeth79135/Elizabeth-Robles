
#OBTENER UN NÚMERO Y DETERMINAR LO SIGUIENTE:
# a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
# b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
# c) en otro caso imprimir No Válido

numero= int(input("Escribe un número: "))


if (numero<0 and numero>-100):
    for i in range(-1,-100,-2):
        print (i)

elif(numero>0 and numero<100):
    for j in range(2,100,2):
        print(j)

elif (numero<=-100 or numero>=100 or numero== 0):
    print("NUMERO INVALIDO")


