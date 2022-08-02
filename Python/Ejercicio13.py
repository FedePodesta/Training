#   EJERCICIO: Tenemos unas descripciones de algunos productos. 
#   En ellas se incluye el precio de cada producto. Debemos encontrar
#   el precio en € y mostrarlo por pantalla. El precio puede tener: 
#   0,1 o 2 decimales y siempre va seguido del símbolo '€'. Por ejemplo: 
#
#       -   9.99€
#       -   10€
#       -   10.5€

#   BONUS: Deberemos modificar las descripciones para que el precio
#   se muestre en dólares. La conversión es: 1€ = 1.21$. No hace falta
#   modificar la variable original de la descripición, podemos retornar
#   una copia con el precio convertido.

des1 = "Este bolso de cuero de la marca: Miguel Cors tiene un precio de 199.99€. Es una oferta especial."
des2 = "Las botas de la marca: Nique valen 89€. Nunca han estado tan rebajadas."
des3 = "¡Tenemos el bambú en oferta! Cómpralo ahora por 1.2€ el kg ¡No la dejes pasar!"

def findPriceAndReplace(txt):
    txtList = txt.split()
    pos = -1
    indx = -1
    conversion = 1.21
    for palabra in txtList:
        pos = palabra.find('€')
        if pos != -1:
            indx = txtList.index(palabra)
            break
    precio =txtList[indx]
    precio = precio.split ('€')[0]
    txtList [indx] = str(float(precio)*conversion) + '$'
    nuevaDescripcion = " ".join(txtList)
    return precio, nuevaDescripcion

precio , descripcion = findPriceAndReplace(des1)
print (precio)
print(descripcion)

precio , descripcion = findPriceAndReplace(des2)
print (precio)
print(descripcion)

precio , descripcion = findPriceAndReplace(des3)
print (precio)
print(descripcion)