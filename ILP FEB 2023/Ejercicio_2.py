
#CALCULAR EL ÁREA Y PERÍMETRO DE UN CÍRCULO

#ENTRADA DE DATOS
radio= float(input("El radio del círculo es de: "))

PI= 3.1416


#PROCESO
perimetro= 2 * PI * radio
area= PI * pow(radio,2)

#SALIDA DE DATOS
print("El área del círculo es = ",round(area,2))
print("El perímetro del círculo es =", round(perimetro,1))


