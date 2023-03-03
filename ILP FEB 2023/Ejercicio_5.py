
#OBTENER VALORES PARA: A, B, C. CALCULAR LA FÓRMULA GENERAL

#ENTRADA DE DATOS
a= float(input("Escribe un valor para a= "))
b= float(input("Escribe un valor para b= "))
c= float(input("Escribe un valor para c= "))


#PROCESO
# b_elevada= pow(b,2)
# multiplicacion_1= 4 * a * c
# multiplicacion_2= 2 * a
# raiz= b_elevada - multiplicacion_1
# resta= -b - raiz
# div= resta / multiplicacion_2

x1= (-b - (pow(   pow(b,2) - (4 * a * c ) , 1/2    )))   /   (2 * a)
x2= (-b + (pow(   pow(b,2) - (4 * a * c ) , 1/2    )))   /   (2 * a)

#SALIDA DE DATOS
print("El resultado de la fórmula x1 es de = ", round(x1, 2))
print("El resultado de la fórmula x2 es de = ", round(x2, 2))


