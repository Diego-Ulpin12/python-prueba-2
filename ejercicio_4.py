def main():
    mostrar = """
    1) Agregar articulo y precio
    2) Terminar
    """
    print(mostrar)
    listaCompra = {}
    precioTotal = 0
    opcion = int(input("¿Desea hacer una lista de compra?: "))
    while opcion != 2:
        cantArti = int(input("¿Cuántos articulos desea comprar?: "))
        for n in range(cantArti):
            articulo = input("Ingrese el articulo: ")
            precio = int(input("Ingrese el precio del articulo: "))
            precioTotal = precioTotal + precio
            listaCompra[articulo] = precio
        print(mostrar)
        opcion = int(input("¿Desea agregar articulos a la lista?: "))
    listaCompra['Total'] = precioTotal
    print(listaCompra)

if __name__ == '__main__':
    main()