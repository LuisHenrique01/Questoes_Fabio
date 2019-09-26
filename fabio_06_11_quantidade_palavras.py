def main():
    texto = str(input('Digite um texto: '))
    print('O texto tem %i palavra(s)'% quantidade_palavras(texto))


def quantidade_palavras(texto):
    palavras = 0
    i = 0
    caracter_anterior = ''
    while i < len(texto):
        caracter = texto[i]
        if caracter == ' ':
            if caracter_anterior != ' ':
                palavras += 1
        caracter_anterior = caracter
        i += 1
    return palavras + 1


if __name__ == '__main__':
    main()
