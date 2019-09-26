def main():
    try:
        n  = int(input('Digite o numero de termos desejados(LEMBRANDO QUE A CONTAGEM DOS TERMOS COMEÇA DO 0): '))
    except:
        print('DIGITE UM NUMERO MAIOR QUE 2!')
        main()
    fibonacci(n)

def fibonacci(n):
    anterio = 0
    atual = 1
    proximo = 1
    print('0 1', end = ' ')
    for i in range(1, n):
        proximo = anterio + atual
        anterio = atual
        atual = proximo
        print(proximo, end = ' ')
    print('')


if __name__ == '__main__':
    main()