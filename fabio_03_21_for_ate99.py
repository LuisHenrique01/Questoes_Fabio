def main():
    print('O valor de S é: {:.2f}'.format(soma_impar()))


def soma_impar():
    b = 1
    s = 0
    for i in range(1, 100, 2):
        s += i / b
        b += 1
    return s


if __name__ == '__main__':
    main()