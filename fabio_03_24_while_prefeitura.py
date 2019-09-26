def main():
    totalassalariados = 0
    totalfilhos = 0
    salarioMil = 0
    totalsalario = 0
    i = 0
    while True:

        salario = int(input('Salario: '))
        filhos = int(input('Quantidade de filhos: '))
        totalassalariados += 1
        totalfilhos += filhos
        totalsalario += salario
        if salario <= 1000:
            salarioMil += 1

        while i != 1 and i != 2:
            i = int(input('Para ler novamente digite 1 - Sim 2 - Não: '))
        if i == 2:
            break
        else:
            i = 0

    mediaSala = totalsalario / totalassalariados
    mediaFilhos = totalfilhos / totalassalariados
    mediaMaior = ((100 * salarioMil) / totalassalariados)

    print('Média de salário da população --- {:.2f}'.format(mediaSala))
    print('Média de número de filhos ------- {:.2f}'.format(mediaFilhos))
    print('Percentual de pessoas com salário de até R$ 1.000,00 ----- {:.2f} %'.format(mediaMaior))


if __name__ == '__main__':
    main()
