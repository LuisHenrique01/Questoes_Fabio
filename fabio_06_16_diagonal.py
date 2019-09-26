from ferramentas_STRING_python import get_ate_vinte
def main():
    texto = get_ate_vinte('Digite um texto com até vinte caracteres.\n')
    diagonal(texto)

def diagonal(texto):
    i = 0
    while i < len(texto):
        espacos = ' ' * i
        print('%s%s'%(espacos,texto[i]))
        i += 1


if __name__ == '__main__':
    main()
