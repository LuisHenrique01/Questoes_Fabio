def main():
    somaSalarioAtual = 0
    somaSalarioRea = 0
    while True:
        salario = float(input('Salario atual: '))
        if salario == 0:
            break
        somaSalarioAtual += salario
        somaSalarioRea += calculaReajuste(salario)
        print('---- NOVO ----')
        print('Novo salario: {:.2f}'.format(calculaReajuste(salario)))
        print('--------------')

    print('----- DADOS FINAIS -----')
    print('Soma dos salarios atuais: {:.2f}'.format(somaSalarioAtual))
    print('Soma dos salarios após reajuste: {:.2f}'.format(somaSalarioRea))
    print('Diferença entre os salarios: {:.2f}'.format(somaSalarioRea - somaSalarioAtual))


def calculaReajuste(salario):
    if salario < 3000:
        salarioRe = (salario * 0.25) + salario
    elif salario < 6000:
        salarioRe = (salario * 0.20) + salario
    elif salario < 10000:
        salarioRe = (salario * 0.15) + salario
    else:
        salarioRe = (salario * 0.10) + salario
    return salarioRe


if __name__ == '__main__':
    main()
