def main():
    populacaoA = int(input('População da cidade A: '))
    indA = float(input('Percetagem da taxa de crescimento da cidade A: '))
    populacaoB = int(input('População da cidade B: '))
    indB = float(input('Percetagem da taxa de crescimento da cidade B: '))

    if (populacaoA > populacaoB and indA > indB) or (populacaoB > populacaoA and indB > indA):
        print('Com os atuais indices de crescimento das duas cidades é impossível a igualdade entre as populações')
    elif populacaoA > populacaoB:
        print('Seram necessario(s) %i anos para a igualdade ou superioridade entre populações'%anosNecessario(populacaoA, indA, populacaoB, indB))
    else:
        print('Seram necessario(s) %i anos para a igualdade ou superioridade entre populações'%anosNecessario(populacaoB, indB, populacaoA, indA))


def anosNecessario(populacaoA, indA, populacaoB, indB):
    anos = 0

    while populacaoA > populacaoB:
        populacaoA = ((indA / 100) * populacaoA) + populacaoA
        populacaoB = ((indB / 100) * populacaoB) + populacaoB
        anos += 1
    return anos


if __name__ == '__main__':
    main()
