def main():
    cand1 = 0
    cand2 = 0
    cand3 = 0
    branco = 0
    nulo = 0
    total = 0
    i = 0
    candidato1 = str(input('Nome do candidato 1: '))
    candidato2 = str(input('Nome do candidato 2: '))
    candidato3 = str(input('Nome do candidato 3: '))
    while True:
        print('1 - {} 2 - {} 3 - {} 0 - Branco 9 - Nulo'.format(candidato1, candidato2, candidato3))
        voto = int(input())
        if voto == 1:
            cand1 += 1
        elif voto == 2:
            cand2 += 1
        elif voto == 3:
            cand3 += 1
        elif voto == 0:
            branco += 1
        else:
            nulo += 1
        total += 1

        while i != 1 and i != 2:
            i = int(input('Para ler novamente digite 1 - Sim 2 - Não: '))
        if i == 2:
            break
        else:
            i = 0
    print('{} obeteve {} voto(s)'.format(candidato1, cand1))
    print('{} obeteve {} voto(s)'.format(candidato2, cand2))
    print('{} obeteve {} voto(s)'.format(candidato3, cand3))
    print('{} voto(s) branco'.format(branco))
    print('{} voto(s) nulo'.format(nulo))
    print('As eleições totalizaram {} voto(s)'.format(total))
    print('{}'.format(vencedor(cand1, cand2, cand3, total, candidato1, candidato2, candidato3)))

def vencedor(cand1, cand2, cand3, total, candidato1, candidato2, candidato3):
    if (total * 0.5) < cand1 or (total * 0.5) < cand3 or (total * 0.5) < cand3:
        print('Vencedor em primeiro turno!')
        if cand1 > cand2 and cand1 > cand3:
            return '{} venceu as eleições presidenciais'.format(candidato1)
        elif cand2 > cand1 and cand2 > cand3:
            return '{} venceu as eleições presidenciais'.format(candidato2)
        else:
            return '{} venceu as eleições presidenciais'.format(candidato3)
    else:
        if cand1 and cand2 > cand3:
            return 'O sengundo turno ocorrera entre os candidatos {} e {}'.format(candidato1, candidato2)
        elif cand2 and cand3 > cand1:
            return 'O sengundo turno ocorrera entre os candidatos {} e {}'.format(candidato2, candidato3)
        elif cand1 and cand3 > cand2:
            return 'O sengundo turno ocorrera entre os candidatos {} e {}'.format(candidato1, candidato3)
        else:
            return 'O segundo turno terá de ser decidido na idade'


if __name__ == '__main__':
    main()
