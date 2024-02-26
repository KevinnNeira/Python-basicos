numero = int(input("Ingrese un numero: "))
if numero > 1:
    for a in range(2, int(numero ** 0.5) + 1):
        if numero % a == 0:
            print(numero, "No es un numero primo") 
            break
    else: 
        print(numero, "Si es un numero primo")
else: print(numero,"No es un numero primo")
            