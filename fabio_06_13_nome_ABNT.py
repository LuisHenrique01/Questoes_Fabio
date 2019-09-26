from ferramentas_STRING_python import pega_sobrenome, my_upper
def main():
    nome = str(input('Nome completo: '))
    ultimo_nome = primeira_letra_sobrenome_maiuscula(nome)
    iniciais = retorna_primeiras_iniciais(nome)

    print('%s, %s'%(ultimo_nome, iniciais))


def retorna_todas_iniciais(nome):
    i = 0
    iniciais = ''
    anterior = ' '
    while i < len(nome):
        if nome[i] != ' ' and anterior == ' ':
            iniciais = iniciais + nome[i] + '.' + ' '
        anterior = nome[i]
        i += 1
    return iniciais


def retorna_primeiras_iniciais(nome):
    i = 0
    primeiras_iniciais = ''
    iniciais = retorna_todas_iniciais(nome)
    while i < len(iniciais)-3:
        primeiras_iniciais = primeiras_iniciais + iniciais[i]
        i += 1
    primeiras_iniciais = my_upper(primeiras_iniciais)
    return primeiras_iniciais


def primeira_letra_sobrenome_maiuscula(nome):
    i = 0
    new_sobrenome = ''
    sobrenome = pega_sobrenome(nome)
    while i < len(sobrenome):
        if i == 0:
            new_sobrenome = my_upper(sobrenome[i])
        else:
            new_sobrenome = new_sobrenome + sobrenome[i]
        i += 1
    return new_sobrenome


if __name__ == '__main__':
    main()
