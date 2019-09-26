def main():
    pesoAntMaior = 0
    pesoAntMenor = 10000
    n = int(input('numero de animais: '))
    for i in range(0, n, 1):
        id = int(input('Numero de indentificação: '))
        nome = str(input('Nome de animal: '))
        peso = float(input('Peso do animal: '))
        if peso > pesoAntMaior:
            pesoAntMaior = peso
            idgordo = id

        if peso < pesoAntMenor:
            pesoAntMenor = peso
            idmagro = id

    print('O animal com maior peso tem %.2f Kg e numero de indentificação %i '%(pesoAntMaior, idgordo))
    print('O animal com menor peso tem %.2f Kg e numero de indentificação %i '%(pesoAntMenor, idmagro))

if __name__ == '__main__':
    main()