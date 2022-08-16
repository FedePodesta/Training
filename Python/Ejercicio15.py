#   EJERCICIOS: Buscador de productos. Tenemos varios productos, el usuario
#   mediante el nombre de un producto puede consultar su precio y sus unidades
#   en stock.


pantalones ={
    "nombre":"pantalones",
    "precio": 39.99,
    "cantidad": 5   
}
chaquetas ={
    "nombre":"chaquetas",
    "precio": 49.99,
    "cantidad": 3   
}
bufandas ={
    "nombre":"bufandas",
    "precio": 9.99,
    "cantidad": 1   
}

productos = [pantalones,chaquetas,bufandas]

def askForInfo(nombreProducto):
    for producto in productos:
        if (producto["nombre"] == nombreProducto):
            return producto["precio"], producto["cantidad"]
            break
    else:
        return 0, 0

nombre= input("Que producto estas buscando? -> ")
precio, cantidad = askForInfo(nombre)
if precio == 0 and cantidad == 0:
    print("Lo sentimos no existe dicho producto")
else:
    print(f"El producto {nombre} vale {precio}$ y tenemos {cantidad} de unidades ")

