def main():
    n = int(input('Digite o numero N: '))
    limiteInfe = int(input('Digite o limite inferior: '))
    limiteSup = int(input('Digite o limite superior: '))

    if limiteSup == 0 or limiteInfe == 0 or (limiteInfe == 0 and limiteSup == 0):
        main()
        print('DIGITE UM INTERVALO VÁLIDO( DIFERENTE DE 0)')
    else:
        mutiplos(n, limiteSup, limiteInfe)


def mutiplos(n, limiteSup, limiteInfe):
    for limiteInfe in range(limiteInfe, limiteSup+1):
        if n % limiteInfe == 0:
            print('O numero %i é multiplo'%(limiteInfe))



if __name__ == '__main__':
    main()