print("Programa que calcula el factorial:")
nm = int(input("Introduzca el numero:"))
factorial = 1
i = 1
while (i <= nm) :
    factorial = factorial * i
    i = i + 1
print("El factorial de: " + str (nm) + " es " + str (factorial))
