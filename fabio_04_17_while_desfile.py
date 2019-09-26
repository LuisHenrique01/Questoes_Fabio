def main():
    nome = str(input('Nome: '))
    magraAnt = 10000
    gordaAnt = 0
    altaAnt = 0
    baixaAnt = 10000
    while nome != 'FIM':
        peso = float(input('Peso: '))
        altura = float(input('Altura: '))
        if magraAnt > peso:
            magraAnt = peso
            nomeMagra = nome
        elif gordaAnt < peso:
            gordaAnt = peso
            nomeGorda = nome

        if altaAnt < altura:
            altaAnt = altura
            nomeAlta = nome
        elif baixaAnt > altura:
            baixaAnt = altura
            nomeBaixa = nome

        nome = str(input('Nome: '))

    print('%s é a cadidata mais alta com %.2f de altura' %(nomeAlta, altaAnt))
    print('%s é a cadidata mais baixa com %.2f de altura' %(nomeBaixa, baixaAnt))
    print('%s é a cadidata mais magra com %.2f de peso' %(nomeMagra, magraAnt))
    print('%s é a cadidata mais gorda com %.2f de peso' %(nomeGorda, gordaAnt))


if __name__ == '__main__':
    main()
