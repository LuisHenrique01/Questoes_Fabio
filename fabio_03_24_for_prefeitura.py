def main():
    totalassalariados = 0
    totalfilhos = 0
    salarioMil = 0
    totalsalario = 0
    n = int(input('Numero de funcionrios: '))
    for i in range(0, n, 1):

        salario = int(input('Salario: '))
        filhos = int(input('Quantidade de filhos: '))
        totalassalariados += 1
        totalfilhos += filhos
        totalsalario += salario
        if salario <= 1000:
            salarioMil += 1

    mediaSala = totalsalario / totalassalariados
    mediaFilhos = totalfilhos / totalassalariados
    mediaMaior = ((100 * salarioMil) / totalassalariados)

    print('Média de salário da população --- %.2f'%(mediaSala))
    print('Média de número de filhos ------- %.2f'%(mediaFilhos))
    print('Percentual de pessoas com salário de até R$ 1.000,00 ----- %.2f %%'%(mediaMaior))


if __name__ == '__main__':
    main()