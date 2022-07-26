
#   EJERCICIO 1: Función máximo -> Dados dos números, la función debe encontrar cuál de los dos
#   es el más grande y retornarlo.Extra: Se deben comprobar que los argumentos de la función sean
#   de tipo int o float. Si alguno de los dos no lo es, mostrar un mensaje de error y retornar False.


def maximo(num1, num2):
    if((type(num1)==int or type(num1)==float) and (type(num2)==int or type(num2)==float)):
        if(num1 > num2):
            return num1
        else:
            return num2
    else:
        print("Los argumentos no son válidos")
        return False

num= maximo(3 , 5)
print( "el numero mayor es: ",num)


