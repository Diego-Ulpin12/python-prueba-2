def kiloMil(valor):
    return valor * 0.621371

def milKilo(valor):
    return valor * 1.60934

def kiloLib(valor):
    return valor * 2.20462

def libKilo(valor):
    return valor * 0.453592

def celFah(valor):
    return (valor * (9/5)) + 32

def fahCel(valor):
    return (valor - 32) * (5/9)

def main():
    menu = """
    1) Kilómetros a Millas
    2) Millas a Kilómetros
    3) Kilogramos a Libras
    4) Libras a Kilogramos
    5) Celsius a Fahrenheit
    6) Fahrenheit a Celsius
    7) Salir
    """
    print(menu)
    opcion = int(input("¿Qué conversión desea realizar?: "))
    unidad = int(input("Ingrese la cantidad que quiere convertir: "))
    while opcion != 7:
        if opcion == 1:
            conversion = kiloMil(unidad)
        elif opcion == 2:
            conversion = milKilo(unidad)
        elif opcion == 3:
            conversion = kiloLib(unidad)
        elif opcion == 4:
            conversion = libKilo(unidad)
        elif opcion == 5:
            conversion = celFah(unidad)
        elif opcion == 6:
            conversion = fahCel(unidad)
        print(f"La conversioón es {conversion}")
        print(menu)
        opcion = int(input("¿Desea hacer otra conversión?: "))

if __name__ =='__main__':
    main()