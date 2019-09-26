def main():
    n = int(input('Digite um numero N: '))

    print('O maior quadrado é %i'%(maior_quadrado(n)))


def maior_quadrado(n):
    anterior = 0
    for i in range(n):
        recente = i**2
        if (recente > anterior) and recente <= n:
            anterior = recente
    return anterior


if __name__ == '__main__':
    main()