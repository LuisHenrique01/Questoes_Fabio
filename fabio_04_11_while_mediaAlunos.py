def main():
    aprovados = 0
    reprovados = 0
    while True:
        matricula = int(input('Matricula: '))
        if matricula == 0:
            break
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        nota3 = float(input('Nota 3: '))
        if media_final(nota1, nota2, nota3) >= 7:
            aprovados += 1
        else:
            reprovados += 1


    print('A sala contem {} aluno(s)'.format(aprovados + reprovados))
    print('Foram {} aprovados'.format(aprovados))
    print('Foram {} reprovados'.format(reprovados))
    print('Uma media de {:.2f} % de aprovados'.format((aprovados*100)/(aprovados+reprovados)))


def media_final(nota1, nota2, nota3):
    media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10
    return media


if __name__ == '__main__':
    main()
