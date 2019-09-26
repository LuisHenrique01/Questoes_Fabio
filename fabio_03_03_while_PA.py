def main():
    r = int(input('Digite a razão da Progressão Aritmética: '))
    a = int(input('Digite o valor de A0: '))
    limite = int(input('Digite o valor limite da PA: '))

    progressao_aritmetica(r, a, limite)

def progressao_aritmetica(r, a, limite):
    while a <= limite:
        print(a, end = ' ')
        a += r
    print('')


if __name__ == '__main__':
    main()
