def calcularAreaTriangulo(base, altura) :
        area = (base * altura) / 2
        return area
  
base = float(input("Ingrese el valor de la base: "))  
altura = float(input("Ingrese el valor de la altura: "))  
area = int(calcularAreaTriangulo(base,altura))
print("El area del triangulo es: ", area)
    