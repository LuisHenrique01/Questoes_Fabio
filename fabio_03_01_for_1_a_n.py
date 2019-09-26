def main():
    n = int(input('Digite um numero N: '))
    contaateN(n)


def contaateN(n):
    for i in range(1, n+1, 1):
        print(i)


if __name__ == '__main__':
    main()
