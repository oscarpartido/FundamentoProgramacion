#1,2,3,4,5,6,7  quieres borrar pares o impares   pares=0    impares=1
#1,3,5,7  imprimir la suma de los valores de la lista
bandera=True
listaPares=[]
listaImpares=[]
sumaPares=0
sumaImpares=0

while bandera:
    num=int(input("ingresa un numero:"))
    if num%2==0:
        listaPares.append(num)
    else:
        listaImpares.append(num)
    
    confirmacion=int(input("quieres ingresar otro numero?"))
    if confirmacion==1:
        bandera=True
    else:
        bandera=False

borrar=int(input("deseas borrrar pares o impares, pares=0 impares=1"))
if borrar==1:
    for valor in listaPares:
        sumaPares+=valor
    print(sumaPares)

    print(listaPares)
elif borrar==0:
    for valor in listaImpares:
        sumaImpares+=valor
    print(listaImpares)
    print(sumaImpares)


