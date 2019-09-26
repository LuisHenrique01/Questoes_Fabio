def main():
    bom = 0
    regular = 0
    totalPessoas = 0
    idadeTotal = 0
    while True:
        idade = int(input('Digite sua idade: '))
        if idade == -1:
            break
        opiniao = int(input('Sua opinião a respeito do filme 1=ótimo, 2=bom, 3=regular, 4=péssimo: '))
        if opiniao == 3:
            regular += 1
        elif opiniao == 2:
            bom += 1
        totalPessoas += 1
        idadeTotal += idade

    print('Media de idade entre as pessoas: %.2f'%(idadeTotal / totalPessoas))
    print('A quantidade de pessoas que respondeu regular: %i' %regular)
    print('o percentual de pessoas que respondeu bom entre os entrevistados: %.2f' %((bom * 100) / totalPessoas), '%')


if __name__ == '__main__':
    main()
