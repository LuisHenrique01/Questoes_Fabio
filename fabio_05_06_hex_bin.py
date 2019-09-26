from vetor_utils import *
def main():
    binario = criar_vetor(8)
    binario = preencher_vetor_inteiros(binario)
    decimal = valor_binario(binario)
    print("O valor em decimal é %d"%decimal)
    hexadecimal = valor_hexadecimal(decimal)
    print("O valor em hexadecimal é %s"%hexadecimal)


def valor_binario(binario):
    decimal = 0
    j = 0
    for i in range(len(binario)-1, -1, -1):
        decimal += binario[i]*2**j
        j += 1 
    return decimal


def valor_hexadecimal(numero):
    hexadecimal = ''
    while numero > 0:
        if numero % 16 < 10:
            hexadecimal = str(numero % 16) + hexadecimal
        else:
            if numero % 16 == 10:
                hexadecimal = 'A' + hexadecimal
            elif numero % 16 == 11:
                hexadecimal = 'B' + hexadecimal
            elif numero % 16 == 12:
                hexadecimal = 'C' + hexadecimal
            elif numero % 16 == 13:
                hexadecimal = 'D' + hexadecimal
            elif numero % 16 == 14:
                hexadecimal = 'E' + hexadecimal
            elif numero % 16 == 15:
                hexadecimal = 'F' + hexadecimal
        numero = numero // 16
    return hexadecimal


if __name__ == "__main__":
    main()