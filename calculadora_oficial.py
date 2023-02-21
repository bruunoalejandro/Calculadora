from __future__ import division
from ipaddress import summarize_address_range


print("Ingrese un numero")
x = float(input())
print("Ingrese operacion")
opc = input()
print("Ingrese otro numero")
y = float(input())
if opc == "+":
    sum = x+y
    print("La suma de los numeros es: ", sum)
if opc == "-" :
    rest = x-y
    print("La resta de los numeros es: ", rest)
if opc == "*" :
    mult = x*y
    print("La multiplicacion de los numeros es: ", mult)
if opc == "/" :
    if y == 0:
        print("No se puede dividir un numero por cero")
    div = x/y
    print("La division de los numeros es: ", div)
