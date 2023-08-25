def numPrimo (numero):
    for n in range(2, numero):
        if numero % n == 0:
            return False
        else:
            return True

def main():
    num_prim = int(input("Ingrese un número: "))
    primo = numPrimo(num_prim)
    print (primo)

if __name__ == '__main__':
    main()