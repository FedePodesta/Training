# Pedir un número por teclado y mostrar los 10 primeros términos de su tabla de multiplicar

numero= int(input("Introduce un numero: "))

for i in range(1,11):
    print(numero,"x",i , "=" , (numero * i))
