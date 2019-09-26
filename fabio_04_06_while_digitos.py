def main():
    num = int(input('Numero: '))
    i = 1
    while num >= 10:
        num = num / 10
        i += 1
    print('O numero contem {} digitos!'.format(i))


if __name__ == '__main__':
    main()
