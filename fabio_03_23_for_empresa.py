def main():
    n = int(input('Numero de funcionrios: '))
    for i in range(0, n, 1):
        nome = str(input('Nome do funcionario: '))
        id = int(input('Numero de indentificação: '))
        horasTraba = int(input('Horas trabalhadas: '))
        nDependentes = int(input('Numero de dependentes: '))

        salarioBru = horasTraba * 12 + nDependentes * 40
        inss = salarioBru * 0.085
        ir = salarioBru * 0.05
        salarioLiquido = salarioBru - (inss + ir)
        print('----- %i -----'%(nome))
        print('Desconto do INSS -------- %.2f'%(inss))
        print('Desconto do ir ---------- %.2f'%(ir))
        print('Salario liquido --------- %.2f'%(salarioLiquido))


if __name__ == '__main__':
    main()