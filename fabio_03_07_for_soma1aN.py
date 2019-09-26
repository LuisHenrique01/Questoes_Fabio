def main():
    n = int(input('Digite um numero N: '))
    print(soma(n))


def soma(n):
    soman = 0
    for i in range(1, n+1):
        soman += i
    return soman


if __name__ == '__main__':
    main()