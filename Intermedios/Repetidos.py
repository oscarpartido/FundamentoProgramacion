#1,2,3,4,1,2,1 decir 1 se repite 3 veces y asi sucesivamente
bandera=True
lista=[]


while bandera:
    num=int(input("ingresa un numero:"))
    lista.append(num)
    confirmacion=int(input("quieres ingresar otro numero?"))
    if confirmacion!=1:
        bandera=False
   
    
    
    
for valor in lista:
    if (lista.count(valor)>=2):
        print(valor, "se repite " ,lista.count(valor))
  
      