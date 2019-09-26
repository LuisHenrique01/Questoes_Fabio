def main():
    i = 1
    idadeF = 0
    idadeM = 0
    homens = 0
    mulheres = 0
    homensSol = 0
    mulheresSol = 0
    acima30 = 0
    while i <= 5:
        sexo = int(input("Sexo (1=Masculino, 2=Feminino): "))
        idade = int(input('Idade: '))
        relacionamento = int(input('Estado civil (1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo): '))
        if sexo == 1:
            idadeM += idade
            homens += 1
            if relacionamento == 2:
                homensSol += 1
        else:
            idadeF += idade
            mulheres += 1
            if relacionamento == 2:
                mulheresSol += 1
            if idade > 30:
                if relacionamento == 3:
                    acima30 += 1
        i += 1

    print('Média de idade das mulheres: %.2f'%(idadeF / mulheres))
    print('Média de idade dos homens: %.2f'%(idadeM / homens))
    print('O percentual de homens solteiros: %.2f'%((homensSol * 100) / homens),'%')
    print('O percentual de mulheres solteiras: %.2f'%((mulheresSol * 100) / mulheres),'%')
    print('quantidade de mulheres divorciadas acima de 30 anos: %i'%acima30)


if __name__ == '__main__':
    main()
