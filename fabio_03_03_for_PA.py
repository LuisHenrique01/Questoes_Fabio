def main():
    r = int(input('Digite a razão da Progressão Aritmética: '))
    a = int(input('Digite o valor de A0: '))
    limite = int(input('Digite o valor limite da PA: '))

    progressao_aritmetica(r, a, limite)

def progressao_aritmetica(r, a, limite):
    for a in range(a, limite, r):
        print(a, end = ' ')
    print('')


if __name__ == '__main__':
    main()