def main():
    i = 0
    while True:
        nome = str(input('Nome do funcionario: '))
        id = int(input('Numero de indentificação: '))
        horasTraba = int(input('Horas trabalhadas: '))
        nDependentes = int(input('Numero de dependentes: '))

        salarioBru = horasTraba * 12 + nDependentes * 40
        inss = salarioBru * 0.085
        ir = salarioBru * 0.05
        salarioLiquido = salarioBru - (inss + ir)
        print('----- {} -----'.format(nome))
        print('Desconto do INSS -------- {:.2f}'.format(inss))
        print('Desconto do ir ---------- {:.2f}'.format(ir))
        print('Salario liquido --------- {:.2f}'.format(salarioLiquido))

        while i != 1 and i != 2:
            i = int(input('Para ler novamente digite 1 - Sim 2 - Não: '))
        if i == 2:
            break
        else:
            i = 0


if __name__ == '__main__':
    main()
