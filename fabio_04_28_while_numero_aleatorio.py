from random import randrange
def main():
    aleatorio = randrange(1000)
    tentativa = int(input("Qual o numero? "))
    while aleatorio != tentativa:
        if aleatorio < tentativa:
            print('Menor')
        else:
            print('Maior')
        tentativa = int(input("Qual o numero? "))

    print('PARABÉNS!!! VOCÊ ACERTOU O NUMERO!!!')


if __name__ == '__main__':
    main()
