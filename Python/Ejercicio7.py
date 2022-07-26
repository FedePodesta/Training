#   Ejercicio: Comprobar si un número introducido por el usuario es par.
#              si el usuario no introduce un número, o el número es decimal
#              el programa debe avisar de que los datos no son correctos.

#Utilizar Not

num = input("Introduce un número: ")

if(not(num.isnumeric())):
    print("Datos incorrectos. El número debe ser un entero")
else:
    num = int(num)
    if(num%2 == 0):
        print("El número es par")
    else:
        print("El número es impar")
    
