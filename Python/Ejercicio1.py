# Pedir 10 números por teclado. summarlos y mostrar el resultado por pantalla

suma=0
for n in range(0,10):
    numero = int(input("Introduce un numero: "))
    suma = suma + numero
print("la suma de todos los numeros ingresados es", suma)

