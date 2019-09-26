def calculadora(tipo, valor1, valor2):
    if tipo == 1:
        soma = valor1 + valor2
        print("A soma corresponde é {:.2f}".format(soma))
    elif tipo == 2:
        sub = valor1 - valor2
        print("A soma corresponde é {:.2f}".format(sub))
    elif tipo == 3:
        multi = valor1 * valor2
        print("A soma corresponde é {:.2f}".format(multi))
    elif tipo == 4:
        div = valor1 / valor2
        print("A soma corresponde é {:.2f}".format(div))
    else:
        print("Digite uma operação valida!")

def main():
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    tipo = int(input("Escolha uma das opções e digite o numero correspondente\n1 – Adição\n2 – Subtração\n3 – Multiplicação\n4 – Divisão\n"))
    calculadora(tipo, valor1, valor2)

if __name__ == '__main__':
    main()
