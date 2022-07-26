# Ejercicio 9:
# Mini calculadora
# Pedirle al usuario una operacion y dos numeros 
# las operaciones pueden ser suma  resta o potencia, si introduce una operacion diferente a estas , mostrar error, si la operacion es correcta mostrar resultado

def calculadora(n1,n2):
    
    n1= int(input("Ingrese un numero: "))
    n2= int(input("Ingrese otro numero: "))
    operacion= int(input("Seleccione una operacion n/1-Suma n/ 2-Resta n/ 3-Potencia: "))
    if operacion != 1 and operacion != 2 and operacion!= 3:
        print("Error debe seleccionar una de la 3 operaciones")
        return
    elif operacion == 1:
            print("la suma de", n1 , " y ", n2 ,"es: ", n1+n2 )
    elif operacion == 2:
        print("la resta de", n1 , " y ", n2 ,"es: ", n1-n2 )
    elif operacion == 3:
        print("la potencia de", n1 , " y ", n2 ,"es: ", n1**n2 )
    else:
        print("error, vuelva a intentarlo")


calculo = calculadora(1,2)
print(calculo)
