def main():
    texto = str(input('Digite um texto:\n'))
    substituir_onde = str(input('Digite a parte a ser substituida: '))
    substitucao = str(input('Digite a nova parte: '))

    print(texto_substituido(texto, substituir_onde, substitucao))


def texto_substituido(texto, substituir_onde, substitucao):
    i = 0
    fim_subs = len(substituir_onde)
    new_texto = ''
    while i < len(texto):
        if texto[i:fim_subs+i] == substituir_onde:
            new_texto = texto[:i] + substitucao + texto[fim_subs+i:]
        i += 1
    return new_texto


if __name__ == '__main__':
    main()
