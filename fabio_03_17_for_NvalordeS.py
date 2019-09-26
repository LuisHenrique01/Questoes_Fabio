def main():
    n = int(input('Digite o valor de N: '))

    print('O valor de S é: %.2f'%(soma_divisor(n)))


def soma_divisor(n):
    s = 0
    for i in range(1, n+1):
        s += 1/i
    return s


if __name__ == '__main__':
    main()