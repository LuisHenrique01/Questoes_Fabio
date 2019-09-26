def main():
    pesoAntMaior = 0
    pesoAntMenor = 10000
    i = 0
    while True:
        id = int(input('Numero de indentificação: '))
        nome = str(input('Nome de animal: '))
        peso = float(input('Peso do animal: '))
        if peso > pesoAntMaior:
            pesoAntMaior = peso
            idgordo = id

        if peso < pesoAntMenor:
            pesoAntMenor = peso
            idmagro = id

        while i != 1 and i != 2:
            i = int(input('Para ler novamente digite 1 - Sim 2 - Não: '))

        if i == 2:
            break
        else:
            i = 0

    print('O animal com maior peso tem {:.2f} Kg e numero de indentificação {} '.format(pesoAntMaior, idgordo))
    print('O animal com menor peso tem {:.2f} Kg e numero de indentificação {} '.format(pesoAntMenor, idmagro))


if __name__ == '__main__':
    main()
