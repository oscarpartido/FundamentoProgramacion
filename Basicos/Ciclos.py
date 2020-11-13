#Imprimir la tabla de multiplicar que el usuario quiera del 1 al 10
# Ejemplo: 1 x n = x

num=int(input("Ingresa el número: "))

for i in range(1, 11):
    multiplicacion = (i*num)
    print(str(i)+ " x " +str(num)+ " = " +str(multiplicacion))
