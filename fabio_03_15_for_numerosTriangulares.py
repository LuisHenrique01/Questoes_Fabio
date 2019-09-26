def main():
    n = int(input('Digite o numero de termos: '))

    pares(n)


def pares(n):
    numero = 0
    print('A senquencia de %i termos é: '%n, end = '')
    for i in range(1, n+1):
        numero += i
        print(numero, end = ' ')
    print('')


if __name__ == '__main__':
    main()