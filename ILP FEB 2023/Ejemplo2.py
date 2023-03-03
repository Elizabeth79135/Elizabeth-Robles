#Operaciones Matemáticas

#Importar librerías o bibliotecas para Funciones Matemáticas
import math

#ENTRADA DE DATOS
#Declarar o crear las variables 
numero_1 = float(input("Escríbe un número: "))
numero_2 = float(input("EScribe otro número: "))

#Declarar una CONSTANTE (elemento que no puede cambiar su valor)
PI = 3.1416

#PROCESOS (Cálculos matemáticos y/o Lógicos)
suma = numero_1 + numero_2
resta = numero_1 - numero_2
mult = numero_1 * numero_2
div = numero_1 / numero_2

potencia_1= numero_1 ** numero_2
potencia_2= pow(numero_1,numero_2)
cuadrado=pow(numero_1, 2)
cubo= pow(numero_2, 3)

raíz_cuadrada_1= math.sqrt(9)
raíz_cuadrada_2= pow(9, 0.5)
raíz_cúbica= pow(27, 1/3)

módulo_residuo= numero_1 % numero_2



#SALIDA DE DATOS
print("La suma es =", suma)
print("La suma es =" + str(suma)) #CONCATENACIÓN (unión de 2 o más textos)
#CASTEO: Conversión de un tipo de dato en otro tipo de dato 
print(f"La suma es = {suma}")
print("La resta es =", resta)
print("La multiplicación es =", mult)
print("La división es =", div)

print("Potencia 1 = ", round(potencia_1, 2))
print("Potencia 2 =", round(potencia_2, 4))
print("Cuadrado =", cuadrado)
print("Cubo =", cubo)

print("Raíz cuadrada 1 =", raíz_cuadrada_1)
print("Raíz cuadrada 2 =", raíz_cuadrada_2)
print("Raíz cubica =", raíz_cúbica)

print("El módulo o residuo =", módulo_residuo)
