def main():
    numero = int(input('Digite o numero secreto: '))
    while True:
        adivinha = int(input('Qual o primeiro numero? '))
        if numero == adivinha:
            break
    print('Parabéns!!!')


if __name__ == '__main__':
    main()
