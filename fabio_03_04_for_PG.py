def main():
    r = int(input('Digite a razão da Progressão Geométrica: '))
    a = int(input('Digite o valor de A0: '))
    limite = int(input('Digite o valor limite da PG: '))

    progressao_aritmetica(r, a, limite)

def progressao_aritmetica(r, a, limite):
    for i in range(a, limite):
        if a <= limite:
            print(a, end = ' ')
        a *= r
    print('')


if __name__ == '__main__':
    main()