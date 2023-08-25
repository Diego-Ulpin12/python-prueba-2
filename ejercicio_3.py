def palindrome(word):
    inversion = word[::-1]
    print(inversion)
    for i in range(len(inversion)):
        if inversion == word:
            return True
        else:
            return False

def main():
    palabra = input("Ingrese una palabra: ")
    print(palabra)
    palindromo = palindrome(palabra)
    print(palindromo)

if __name__ == '__main__':
    main()
    #No se me ocurrio como solucionarlo. No me acuerdo. Sorry :(