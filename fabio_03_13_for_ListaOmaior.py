def main():
    n = int(input('Digite o numero de numeros para efetuar a media: '))
    lista = input('Digite os numeros: ').split(' ')

    print('O maior valor é %i'%(maior(n, lista)))

def maior(n, lista):
    anterior = 0
    for i in range(n):
        recente = int(lista[i])
        if recente > anterior:
            anterior = recente
    return anterior


if __name__ == '__main__':
    main()