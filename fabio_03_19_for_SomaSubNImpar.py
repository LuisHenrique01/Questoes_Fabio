def main():
    n = int(input('Digite o valor de N: '))

    print('O valor de S é: %.2f'%(soma_Sub(n)))


def soma_Sub(n):
    soma = 0
    sub = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            soma += i/(n-(i-1))
        else:
            sub += ((n-(i-1))/i)*(-1)
    return sub + soma


if __name__ == '__main__':
    main()