def main():
    id = int(input('Numero de indentificação: '))
    peso = int(input('Peso do animal: '))
    magro = peso+1
    gordo = peso-1
    while id != 0:
        if magro > peso:
            magro = peso
            idMagro = id
        elif gordo < peso:
            gordo = peso
            idGordo = id
        id = int(input('Numero de indentificação: '))
        peso = int(input('Peso do animal: '))
    print('O animal de ID %i é o mais magro com %i' %(idMagro, magro))
    print('O animal de ID %i é o mais gordo com %i' %(idGordo, gordo))


if __name__ == '__main__':
    main()
