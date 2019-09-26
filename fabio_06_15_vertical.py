from ferramentas_STRING_python import get_ate_vinte, get_coluna
def main():
    texto = get_ate_vinte('Digite um texto com até vinte caracteres.\n')
    coluna = get_coluna('Digite a culona até 20: ')
    vertical(coluna, texto)


def vertical(coluna, texto):
    i = 0
    espacos = (coluna - 1) * ' '
    while i < len(texto):
        print('%s%s'%(espacos, texto[i]))
        i += 1


if __name__ == '__main__':
    main()
