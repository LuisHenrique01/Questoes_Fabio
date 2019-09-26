def main():
    cand1 = 0
    cand2 = 0
    cand3 = 0
    branco = 0
    nulo = 0
    total = 0
    candidato1 = str(input('Nome do candidato 1: '))
    candidato2 = str(input('Nome do candidato 2: '))
    candidato3 = str(input('Nome do candidato 3: '))
    n = int(input('Numero de eleitores: '))
    for i in range(0, n, 1):
        print('1 - %s 2 - %s 3 - %s 0 - Branco 9 - Nulo'%(candidato1, candidato2, candidato3))
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
    print('%s obeteve %i voto(s)'%(candidato1, cand1))
    print('%s obeteve %i voto(s)'%(candidato2, cand2))
    print('%s obeteve %i voto(s)'%(candidato3, cand3))
    print('%i voto(s) branco'%(branco))
    print('%i voto(s) nulo'%(nulo))
    print('As eleições totalizaram %i voto(s)'%(total))
    print('%s'%(vencedor(cand1, cand2, cand3, branco, nulo, total, candidato1, candidato2, candidato3)))

def vencedor(cand1, cand2, cand3, branco, nulo, total, candidato1, candidato2, candidato3):
    if (total * 0.5) < cand1 or (total * 0.5) < cand3 or (total * 0.5) < cand3:
        print('Vencedor em primeiro turno!')
        if cand1 > cand2 and cand1 > cand3:
            return '%s venceu as eleições presidenciais'%(candidato1)
        elif cand2 > cand1 and cand2 > cand3:
            return '%s venceu as eleições presidenciais'%(candidato2)
        else:
            return '%s venceu as eleições presidenciais'%(candidato3)
    else:
        if cand1 and cand2 > cand3:
            return 'O sengundo turno ocorrera entre os candidatos %s e %s'%(candidato1, candidato2)
        elif cand2 and cand3 > cand1:
            return 'O sengundo turno ocorrera entre os candidatos %s e %s'%(candidato2, candidato3)
        elif cand1 and cand3 > cand2:
            return 'O sengundo turno ocorrera entre os candidatos %s e %s'%(candidato1, candidato3)
        else:
            return 'O segundo turno terá de ser decidido na idade'


if __name__ == '__main__':
    main()