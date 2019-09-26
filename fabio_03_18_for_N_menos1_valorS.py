def main():
    n = int(input('Digite o valor de N: '))

    print('O valor de S é: %.2f'%(soma_divisorMenos1(n)))


def soma_divisorMenos1(n):
    s = 0
    for i in range(1, n+1):
        s += i/(n-(i-1))
    return s


if __name__ == '__main__':
    main()