#Llenar lista con un while y parar el llenado de la lista hasta escribir el número sea negativo

lista=[]
bandera = True
while bandera:
    num=int(input("Ingresa el número: "))

    if (num<0):
        bandera = False

    else:
        lista.append(num)

print(lista)