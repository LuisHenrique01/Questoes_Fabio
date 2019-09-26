def main():
    n = int(input('Digite o valor de N: '))

    print('O valor de S é: {:.2f}'.format(soma_impar(n)))


def soma_impar(n):
    i = 1
    s = 0
    soma = 0
    sub = 0
    while n >= i:
        if i % 2 != 0:
            soma += 1/i
            i += 1
        else:
            sub += (1/i)*(-1)
            i += 1
    s = sub + soma
    return s


if __name__ == '__main__':
    main()
