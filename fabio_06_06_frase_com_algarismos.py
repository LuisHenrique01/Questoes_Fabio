def main():
    frase = str(input('Digite um texto: '))
    print(frase_final(frase))


def frase_final(frase):
    i = 0
    frase_final = ''
    while i < len(frase):
        caracter = frase[i]
        frase_final = frase_final + numero_extenso(caracter, i)
        i += 1
    return frase_final


def numero_extenso(caracter, i):
    j = 0
    nome = ''
    if caracter == '1':
        nome_numero = 'um'
    elif caracter == '2':
        nome_numero = 'dois'
    elif caracter == '3':
        nome_numero = 'três'
    elif caracter == '4':
        nome_numero = 'quatro'
    elif caracter == '5':
        nome_numero = 'cinco'
    elif caracter == '6':
        nome_numero = 'seis'
    elif caracter == '7':
        nome_numero = 'sete'
    elif caracter == '8':
        nome_numero = 'oito'
    elif caracter == '9':
        nome_numero = 'nove'
    elif caracter == '0':
        nome_numero = 'zero'
    else:
        return caracter
    if i == 0:
        while j < len(nome_numero):
            caracterRes = nome_numero[j]
            if j == 0:
                nome = nome + caracterRes.upper()
            else:
                nome = nome + caracterRes
            j += 1
        nome_numero = nome
    else:
        nome_numero = ' ' + nome_numero
    return nome_numero


if __name__ == '__main__':
    main()
