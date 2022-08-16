''' Ejercicio 7:
    Queremos comparar el tiempo que tarda en sumar todos los elementos de una lista un bucle for y un bucle while.

    debemos calcular el tiempo empleado en cada bucle varias veces y luego promediarlo.
    Debemos cronometrar lo que tarda cada bucle 100 veces y guardar en un fichero.'''


import time
import random
#   lista que deberemos sumar
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(50000):
    lista.append(random.randint(0, 10000))
fichero = open('times.txt', 'wt', encoding='utf-8')


#   Paso 1: Recopilar y escribir los datos
for x in range(100):
    #   suma total para el bucle for
    accFor = 0
    startTime = time.time()
    for num in lista:
        accFor = accFor + num
    elapsedTimeFor = time.time() - startTime 

    pos = 0
    #   suma total para el bucle while
    accWhile = 0
    startTime = time.time()
    while pos < len(lista):
        accWhile = accWhile + lista[pos]
        pos = pos + 1
    elapsedTimeWhile = time.time() - startTime
    fichero.write(f"{elapsedTimeFor};{elapsedTimeWhile}\n")
fichero.close()


#   Paso 2: Leer datos y calcular el tiempo medio

fichero = open('times.txt', 'rt', encoding='utf-8')

meanFor = 0
meanWhile = 0
samples = 0

for line in fichero.readlines():
    line.replace('\n','')
    timeFor, timeWhile = line.split(';')
    meanFor += float(timeFor)
    meanWhile += float(timeWhile)
    samples += 1

print(f"Tiempo medio bucle for: {(meanFor/samples)*(10**3)}ms. Tiempo medio bucle while: {(meanWhile/samples)*(10**3)}ms")

fichero.close()