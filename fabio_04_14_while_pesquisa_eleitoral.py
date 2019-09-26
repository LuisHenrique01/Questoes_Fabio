def main():
    voto = 0
    serra = 0
    dilma = 0
    ciro = 0
    indeciso = 0
    outros = 0
    nulos = 0
    total = 0
    while voto != -1:
        voto = int(input('Serra=45, Dilma=13, Ciro Gomes=23, indeciso=99, outros=98, nulo/branco=0:\n'))
        if voto == 45:
            serra += 1
        elif voto == 13:
            dilma += 1
        elif voto == 23:
            ciro += 1
        elif voto == 99:
            indeciso += 1
        elif voto == 98:
            outros += 1
        else:
            nulos += 1
        total += 1

    print("--- SERRA ---")
    print('%.2f' % (serra * 100 / total))
    print("--- DILMA ---")
    print('%.2f' % (dilma * 100 / total))
    print("--- CIRO GOMES ---")
    print('%.2f' % (ciro * 100 / total))
    print("--- OUTROS ---")
    print('%.2f' % (outros * 100 / total))
    print("--- INDECESOS ---")
    print('%.2f' % (indeciso * 100 / total))
    print("--- NULOS/BRANCOS ---")
    print('%.2f' % (nulos * 100 / total))
    print(segundoTurno(serra, dilma, ciro, outros, total))

def segundoTurno(serra, dilma, ciro, outros, total):
    if  (total * 0.5) < serra or (total * 0.5) < dilma or (total * 0.5) < ciro or (total * 0.5) < outros:
        return 'Não haverá segundo turno'
    else:
        return 'Chance de segundo turno entre os dois candidatos com melhor porcentagem'


if __name__ == '__main__':
    main()
