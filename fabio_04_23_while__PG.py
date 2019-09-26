def main():
    razao = int(input('Razão da PG: '))
    primeiro_termo = int(input('Primeiro termo: '))
    termos = int(input('Termos: '))

    progressao_geometrica(razao, primeiro_termo, termos)


def progressao_geometrica(razao, primeiro_termo, termos):
    while termos > 0:
        print(primeiro_termo, end = ' ')
        primeiro_termo *= razao
        termos -= 1
    print('')


if __name__ == '__main__':
    main()
