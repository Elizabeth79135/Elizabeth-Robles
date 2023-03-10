
#PEDIR EL NIVEL DEL AGUA EN METROS DE UNA CISTERNA


niveldelagua= int(input("Escribe el nivel del agua= "))

if (niveldelagua>6):
    print("DESBORDAMIENTO DEL AGUA EN LA CISTERNA")
elif(niveldelagua==6):
    print("APAGAR LA BOMBA")
elif(niveldelagua>4 and niveldelagua<6):
    print("DESACELERAR BOMBA")
elif(niveldelagua>2 and niveldelagua<4):
    print("BOMBA TRABAJANDO!")
elif(niveldelagua>0 and niveldelagua<2):
    print("ACELERAR BOMBA DE AGUA")
elif(niveldelagua==0):
    print("ENCENDER BOMBA DE AGUA")
elif(niveldelagua<0):
    print("FUGA EN CISTERNA")
