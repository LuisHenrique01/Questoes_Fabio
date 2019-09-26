def main():
    n = int(input('Digite o valor de N: '))

    print('O valor de S é: {:.2f}'.format(soma_divisorMenos1(n)))


def soma_divisorMenos1(n):
    i = 1
    s = 0
    a = 0
    while n >= i:
        s += i/(n-a)
        i += 1
        a += 1
    return s


if __name__ == '__main__':
    main()
