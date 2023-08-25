def main():
    palabra = input("Ingrese una palabra: ")
    letra = input("Ingrese letra a contar: ")
    cont = 0
    for i in range(len(palabra)):
        if letra in palabra[i]:
            cont = cont + 1
    print(f"La letra {letra} esta {cont} en {palabra}")

if __name__ == '__main__':
    main()