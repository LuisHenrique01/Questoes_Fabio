def main():
    limiteInfe = int(input('Digite o limite inferior: '))
    limiteSup = int(input('Digite o limite superior: '))

    numeros_entre_intervalo(limiteSup, limiteInfe)


def numeros_entre_intervalo(limiteSup, limiteInfe):
    print('Os primos entre os limites são: ', end = '')
    for limiteInfe in range(limiteInfe, limiteSup+1):
        if primos(limiteInfe):
            print(limiteInfe, end = ' ')
    print('')


def primos(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



if __name__ == '__main__':
    main()