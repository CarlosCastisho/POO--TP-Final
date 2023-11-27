from circulo import Circulo
from rectangulo import Rectangulo
from triangulo import Triangulo

while True:
    print("___________________________________________________")
    print("             Menú de Opciones")
    print(" 1. Calcular área y perímetro de un Círculo")
    print(" 2. Calcular área y perímetro de un Rectángulo")
    print(" 3. Calcular área y perímetro de un Triángulo")
    print(" 4. Salir\n")

    opt = input("Seleccione una Opción: ")
    print("___________________________________________________")

    if opt == "1":
        radio_circulo = float(input("Ingrese el radio: "))
        calcirculo = Circulo(radio_circulo)
        print("___________________________________________________")
        print(f"    EL area del circulo es: {calcirculo.area()}")
        print(f"    EL perimetro del circulo es: {calcirculo.perimetro()}")
        print("___________________________________________________")

    elif opt == "2":
        base_rect = float(input("Ingrese la base: "))
        altura_rect = float(input("Ingrese la altura: "))
        calrect = Rectangulo(base_rect, altura_rect)
        print("___________________________________________________")
        print(f"    EL area del rectangulo es: {calrect.area()}")
        print(f"    EL perimetro del rectangulo es: {calrect.perimetro()}")
        print("___________________________________________________")

    elif opt =="3":
        base_triang = float(input("Ingrese la base: "))
        alt_triang = float(input("Ingrese la altura: "))
        lado1_triang = float(input("Ingrese el primer lado: "))
        lado2_triang = float(input("Ingrese el segundo lado: "))
        caltriang = Triangulo(base_triang, alt_triang, lado1_triang, lado2_triang)
        print("___________________________________________________")
        print(f"    EL area del rectangulo es: {caltriang.area()}")
        print(f"    EL perimetro del rectangulo es: {caltriang.perimetro()}")
        print("___________________________________________________")
    
    elif opt == "4":
        break

    else:
        print("Seleccione una opcion validad o seleccione 4 para salir")