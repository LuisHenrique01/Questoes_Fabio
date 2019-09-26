def main():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))
    print('%i * %i = %i' %(a, b, multiplicacao(a, b)))


def multiplicacao(a, b):
    multi = 0
    while a > 0:
        multi += b
        a -= 1
    return multi


if __name__ == '__main__':
    main()
