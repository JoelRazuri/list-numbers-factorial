"""  
    Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el usuario,
    a cada uno le calcule el factorial e imprima el resultado junto con el número de orden correspondiente.
"""

lista = []
numero = 1

while (numero!=-1):
    numero = int(input("Ingrese una serie de numeros, de uno en uno (-1 para salir):"))
    if numero>=0:
        lista.append(numero)

print("")

for i in range(len(lista)):
    factorial=1
    for j in range(2,lista[i]+1):
        factorial=factorial*j

    print(f"Número: {lista[i]} - Factorial: {factorial}")


