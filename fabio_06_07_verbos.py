def main():
    verbo = get_verbo('Digite um verbo regular com terminção em ER: ')
    printa_conjugacao_dos_verbos(verbo)


def get_verbo(mensagem):
    verbo = str(input(mensagem))
    terminacao = verbo[len(verbo) - 2] + verbo[len(verbo) - 1]
    if terminacao.upper() == 'ER':
        return verbo
    else:
        print('Digite um verbo terminado em ER!!')
        return get_verbo(mensagem)


def printa_conjugacao_dos_verbos(verbo):
    i = 0
    radical = ''
    while i < len(verbo):
        caracter = verbo[i]
        if i < len(verbo) - 2:
            radical = radical + caracter
        i += 1

    print('Eu',radical+'o')
    print('Tu',radical+'es')
    print('Ele',radical+'e')
    print('Nós',radical+'emos')
    print('Vós',radical+'eis')
    print('Eles',radical+'em')


if __name__ == '__main__':
    main()
