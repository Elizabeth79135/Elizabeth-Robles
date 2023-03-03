
#PEDIR LA CANTIDAD DE GRADOS Y CONVERTIRLOS A °C, °F Y °K

#ENTRADA DE DATOS
grados= float(input("Escribe el grado a convertir= "))


#PROCESO
celsius_1= grados - 273.15
celsius_2= (5 * (grados - 32)) / 9
# fahrenheit_1= 9 * grados / 5 + 2
# fahrenheit_2= 9 * grados - 273.15 / 5 + 32
# kelvin_1= grados + 273.15
# kelvin_2= 5 * grados - 32 / 9 + 273.15


#SALIDA DE DATOS
print("El grado de K a C es de = ",round(celsius_1,2))
print("El grado de F a C es de = ",round(celsius_2,2))
# print("El grado de C a F es de =", round(fahrenheit_1,2))
# print("El grado de K a F es de =", round(fahrenheit_2,2))
# print("El grado de C a K es de =", round(kelvin_1,2))
# print("El grado de F a K es de =", round(kelvin_2,2))