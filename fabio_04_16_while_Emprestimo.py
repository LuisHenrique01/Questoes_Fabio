def main():
    emprestimo = int(input('Valor do impestimo: '))
    parcelas = int(input('Valor das parcelas: '))

    print('Você pagará o emprestimo em %i dias' %dias_uteis(emprestimo, parcelas))


def dias_uteis(emprestimo, parcelas):
    dias = 0
    while emprestimo > 0:
        emprestimo = (emprestimo - (emprestimo * 0.0085)) - parcelas
        dias += 1
    return dias


if __name__ == '__main__':
    main()
