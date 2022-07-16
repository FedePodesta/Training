# Pedir números al usuario hasta que introduzca uno negativo.Al finalizar mostrar la cantidad  de números introducidos sin contar el negativo.


numero= 0
contador= 0
while numero >=0:
    numero = int(input("introduce un numero:"))
    if numero >= 0:
        contador += 1
    
    

print("se han introducido", contador ,  "numeros")

