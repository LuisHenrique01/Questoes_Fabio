def main():
    n = int(input('Digite o numero de numeros para efetuar a media: '))
    lista = input('Digite os numeros: ').split(' ')
    print('A soma é igual a %i'%(soma(n, lista)))
    print('A media é igual a %.2f'%(media(n, lista)))


def soma(n, lista):
    somaN = 0
    for i in range(n):
        somaN += int(lista[i])
    return somaN


def media(n, lista):
    return soma(n, lista) / n


if __name__ == '__main__':
    main()