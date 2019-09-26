def main():
    nome1 = str(input('Nome do jogador 1: '))
    nome2 = str(input('Nome do jogador 2: '))
    player1 = 0
    player2 = 0
    while True:
        cod = int(input('Ponto para jogador 1 ou 2? '))
        if cod == 1:
            player1 += 1
        elif cod == 2:
            player2 += 1
        else:
            print('CÓDIGO ERRADO!!!')

        if ja_ganhou(player1, player2):
            if player1 > player2:
                vencedor = nome1
                break
            else:
                vencedor = nome2
                break

        print('-------PLACAR-------')
        print('{} ---- {}'.format(nome1, player1))
        print('{} ---- {}'.format(nome2, player2))

    print('-------PLACAR FINAL-------')
    print('{} ---- {}'.format(nome1, player1))
    print('{} ---- {}'.format(nome2, player2))
    print('O jogador {} é o vencedor!!!'.format(vencedor))

def ja_ganhou(player1, player2):
    if player1 > player2:
        maior = player1
        menor = player2
    else:
        maior = player2
        menor = player1
    return maior >= 21 and (maior - menor) >= 2


if __name__ == '__main__':
    main()
