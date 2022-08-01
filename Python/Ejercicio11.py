#   ENUNCIADO: Tenemos un texto dónde queremos encontrar palabras clave. 
#   Las palabras clave pueden ser hasta 5 y deberemos pedírselas al usuario 
#   y guardarlas en una lista. 

#   Si el usuario quiere poner menos de 5 palabras clave, deberá escribir 
#   "fin" para terminar de introducir datos. Si el usuario introduce 
#   números o nada, deberemos eliminarlos de la lista antes de la búsqueda.

#   En otra lista, deberemos guardar el número de veces que aparece cada 
#   palabra clave en nuestro texto. Por ejemplo, si las palabras clave son
#   ordenador y portátil y aparecen 5 y 7 veces respectivamente, nuestras listas
#   deberían ser así: 
#       -   keywords = ["ordenador", "portátil"]
#       -   ocurrencias = [5, 7]


#   Pista: Podemos pasar de una cadena de texto a una lista de palabras mediante
#   el método texto.split(). Por ejemplo:
# texto = "hola que tal"
# print(texto.split())    

texto = """"Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa. 
Es muy importante que logremos teletrabajar efectivamente y de manera autorregulada. 
Esto se traduce en finalizar antes nuestras tareas y evitar jornadas laborales interminables.
El primer consejo y uno de los más importantes ya te lo he dado en el apartado anterior. 
Tenemos que construir un espacio de trabajo en el que nos sintamos cómodos y dispongamos de todas las herramientas necesarias para teletrabajar. 
En la medida de lo posible, es importante teletrabajar siempre en el mismo lugar. 
De esta forma, nuestro cerebro asocia el sitio con la acción de trabajar y nos hará estar más focalizados en nuestras tareas.""" 

#   Obtener palabras clave
keywords = []
ocurrencias = []

for x in range(5):
    keyword = input("Introduce una palabra clave. Si no quieres escribe 'fin': ")
    if keyword == "fin":
        break
    else:
        keywords.append(keyword)

print("Palabras clave introducidas: ")
print(keywords)

posicion = 0

while(True):
    if posicion >= len(keywords):
        break
    if keywords[posicion] == '': 
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric():
        keywords.pop(posicion)
    else:
        posicion += 1


print("Palabras clave corregidas: ")
print(keywords)


texto = texto.replace('.', '').replace(',', '').split()


for x in range(len(keywords)):
    ocurrencias.append(0)

print("Lista de ocurrencias inicializada: ")
print(ocurrencias)

for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            posicion = keywords.index(keyword)
            ocurrencias[posicion] += 1
            break

print("Resultado final: ")
print(keywords)
print(ocurrencias)