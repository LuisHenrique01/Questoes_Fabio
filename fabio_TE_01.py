def main():
    numero = int(input('Digite um numero de dois digitos: '))
    dezena = numero // 10
    unidade = numero % 10
    if dezena == unidade:
        print('A dezena e a unidade são iguais!')
    else:
        print('A dezena e a unidade não são iguais!')


if __name__ == "__main__":
    main()

