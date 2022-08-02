#   EJERCICIO: Formatear texto. Debemos formatear el siguiente texto siguiendo 
#   una serie de normas: 
#       -   '#' a principio de línea significa que es un título y deberemos convertirlo 
#           todo a mayúsculas.
#       -   '##' a principio de línea significa que es un subtítulo y deberemos poner la
#            primera letra de cada palabra en mayúsculas.
#       -   '###' deberemos poner únicamente la primera letra en mayúsculas.
#       -   si la línea empieza con '-' deberemos añadir una sangría.

#   NOTA: El método splitlines() retorna una lista de strings. Separa mediante saltos de línea.
#   SOLUCIÓN:


texto = """
#este es el título principal

- Esto es una lista.
- De cosas que podemos hacer.

##este es un subtítulo

Esto es una pequeña introducción.
- Esto es otra lista
- De más cosas que podemos hacer.
"""

def formatText(texto):
    listaTexto = texto.splitlines()
    for indx in range(len(listaTexto)):
        if (listaTexto[indx].startswith("###")):
            listaTexto[indx] = listaTexto[indx].replace("###", "")
            listaTexto[indx] = listaTexto[indx].capitalize()
        elif (listaTexto[indx].startswith("##")):
            listaTexto[indx] = listaTexto[indx].replace("##", "")
            listaTexto[indx] = listaTexto[indx].title()
        elif (listaTexto[indx].startswith("#")):
            listaTexto[indx] = listaTexto[indx].replace("#", "")
            listaTexto[indx] = listaTexto[indx].upper()
        elif (listaTexto[indx].startswith("-")):
            listaTexto[indx] = listaTexto[indx].rjust(len(listaTexto[indx])+ 8)
    return "\n".join(listaTexto)


print (formatText(texto))