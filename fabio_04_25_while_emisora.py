def main():
    canal2 = 0
    canal4 = 0
    canal5 = 0
    canal7 = 0
    canal10 = 0
    outros = 0
    total = 0
    while True:
        canal = int(input('Digite o canal escolhido(2, 4, 5, 7, 10): '))
        if canal == 0:
            break
        elif canal == 2:
            canal2 += 1
        elif canal == 4:
            canal4 += 1
        elif canal == 5:
            canal5 += 1
        elif canal == 7:
            canal7 += 1
        elif canal == 10:
            canal10 += 1
        else:
            outros += 1
        total += 1

    print('Canal 2: %.2f' %((canal2 * 100) / total), '%')
    print('Canal 4: %.2f' %((canal4 * 100) / total), '%')
    print('Canal 5: %.2f' %((canal5 * 100) / total), '%')
    print('Canal 7: %.2f' %((canal7 * 100) / total), '%')
    print('Canal 10: %.2f' %((canal10 * 100) / total), '%')
    print('Outros ou nenhum canal: %.2f' %((outros * 100) / total), '%')
    print('Total intrevistados: %i' %total)


if __name__ == '__main__':
    main()
