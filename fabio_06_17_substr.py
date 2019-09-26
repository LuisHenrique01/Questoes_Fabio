def main():
    texto = str(input('Digite o texto:\n'))
    inicio = int(input('Digite o local de inicio: '))
    qtd_caracteres = int(input('Quantidade de caracteres: '))
    print('%s'%vinte_carcteres(texto, inicio, qtd_caracteres))


def vinte_carcteres(texto, inicio, qtd_caracteres):
    i = 0
    j = 0
    new_texto = ''
    if qtd_caracteres > len(texto) - inicio:
        qtd_caracteres = len(texto) - inicio
    while i < len(texto):
        if i >= (inicio - 1) and j <= (qtd_caracteres - 1):
            new_texto = new_texto +  texto[i]
            j += 1
        i += 1
    return new_texto


if __name__ == '__main__':
    main()
