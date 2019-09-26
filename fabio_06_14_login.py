from ferramentas_STRING_python import retorna_todas_iniciais, e_letra
def main():
    nome = str(input('Nome completo: '))
    print('Seu login: %s'%gera_login(nome))


def gera_login(nome):
    iniciais = retorna_todas_iniciais(nome)
    i = 0
    login = ''
    while i < len(iniciais):
        if e_letra(iniciais[i]):
            login = login + iniciais[i]
        i += 1
    return login


if __name__ == '__main__':
    main()
