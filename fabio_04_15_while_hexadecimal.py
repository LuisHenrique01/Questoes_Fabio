def main():
    n = int(input('Digite um numero entre 0 e 255: '))
    while n < 0 or n > 255:
        n = int(input('Digite um numero entre 0 e 255: '))

    contBi = n
    contHex = n
    if n == 0:
        print('Base binaria = 0')
        print('Base hexadecimal = 0')
    else:
        print('Base binaria = %s' % valorBinario(contBi))
        print('Base hexadecimal = %s' % valorHexadecimal(contHex))


def valorBinario(contBi):
    numBinario = ''
    while contBi > 0:
        numBinario = str(contBi % 2) + numBinario
        contBi = contBi // 2
    return numBinario


def valorHexadecimal(contHex):
    numHexa = ''
    while contHex > 0:
        if contHex % 16 < 10:
            numHexa = str(contHex % 16) + numHexa
        else:
            if contHex % 16 == 10:
                numHexa = 'A' + numHexa
            elif contHex % 16 == 11:
                numHexa = 'B' + numHexa
            elif contHex % 16 == 12:
                numHexa = 'C' + numHexa
            elif contHex % 16 == 13:
                numHexa = 'D' + numHexa
            elif contHex % 16 == 14:
                numHexa = 'E' + numHexa
            elif contHex % 16 == 15:
                numHexa = 'F' + numHexa
        contHex = contHex // 16
    return numHexa


if __name__ == '__main__':
    main()
