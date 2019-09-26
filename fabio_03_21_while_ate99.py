def main():
    print('O valor de S é: {:.2f}'.format(soma_impar()))


def soma_impar():
    a = 1
    b = 1
    s = 0
    while a <= 99:
        s += a / b
        a += 2
        b += 1
    return s


if __name__ == '__main__':
    main()
