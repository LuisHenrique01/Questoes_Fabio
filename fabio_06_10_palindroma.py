def main():
    palavra = str(input('Digite uma palavra: '))
    if e_palidroma(palavra):
        print('É palíndroma!')
    else:
        print('Não é palíndroma!')


def e_palidroma(palavra):
    return palavra[::-1].upper() == palavra.upper()


if __name__ == '__main__':
    main()
