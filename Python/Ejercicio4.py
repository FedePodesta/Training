#Pedir dos números por teclado y mostrar todos los números pares comprendidos entre ambos.


numero1= int(input("Introduce el primer numero: "))
numero2=numero1
while numero2 <= numero1:
    numero2= int(input("Introduce un  numero mayor al anterior: "))



for n in range(numero1, numero2+1):
    if n % 2 == 0:
        print(n)