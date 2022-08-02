#   EJERCICIO (mini): Tenemos un string únicamente compuesto por números enteros. 
#   Debemos sumar su valor uno a uno y mostrar por pantalla la suma
#   total de todos los números.

numeros = "1221321213"
total =0
for n in numeros:
    total+= int(n)
else:
    print ("el valor total es: " + str(total))