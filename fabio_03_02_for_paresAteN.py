def main():
    n = int(input('Digite um numero N: '))
    pares_ate_N(n)


def pares_ate_N(n):
    for i in range(1, n+1, 1):
        if i % 2 == 0:
            print(i)


if __name__ == '__main__':
    main()