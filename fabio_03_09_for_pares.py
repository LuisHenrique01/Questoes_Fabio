def main():
    limiteInfe = int(input('Digite o limite inferior: '))
    limiteSup = int(input('Digite o limite superior: '))

    pares(limiteSup, limiteInfe)


def pares(limiteSup, limiteInfe):
    print('Os pares entre os limites são: ', end = '')
    for limiteInfe in range(limiteInfe, limiteSup+1):
        if limiteInfe % 2 == 0 :
            print(limiteInfe, end = ' ')
    print('')


if __name__ == '__main__':
    main()