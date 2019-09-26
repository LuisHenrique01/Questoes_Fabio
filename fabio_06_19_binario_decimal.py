from ferramentas_STRING_python import get_binario
def main():
    num_binario = get_binario('Numero em binario: ')
    print('Numero em decimal: %i'%corverte_binario(num_binario))


def corverte_binario(num_binario):
    i = len(num_binario) - 1
    decimal = 0
    expoente = 0
    while i >= 0:
        num = int(num_binario[i])
        decimal += num * (2**expoente)
        i -= 1
        expoente += 1
    return decimal


if __name__ == '__main__':
    main()
