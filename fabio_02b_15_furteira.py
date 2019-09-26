def precofrutaria(macaKG, morangoKG):
    KGtotal = morangoKG + macaKG
    if KGtotal <= 5:
        preco = (morangoKG * 2.50) + (macaKG * 1.80)
        if preco > 25:
            preco = preco - (preco * 0.10)
            print("Total a ser pago: R$ {:.2f}".format(preco))
        else:
            print("Total a ser pago: R$ {:.2f}".format(preco))
    elif KGtotal <= 8:
        preco = (morangoKG * 2.20) + (macaKG * 1.50)
        if preco > 25:
            preco = preco - (preco * 0.10)
            print("Total a ser pago: R$ {:.2f}".format(preco))
        else:
            print("Total a ser pago: R$ {:.2f}".format(preco))
    else:
        preco = (morangoKG * 2.20) + (macaKG * 1.50)
        preco = preco - (preco * 0.10)
        print("Total a ser pago: R$ {:.2f}".format(preco))


def main():
    morangoKG = float(input("Digite a quantidade de morango em KG: "))
    macaKG = float(input("Digite a quantidade de maçã em KG: "))
    precofrutaria(macaKG, morangoKG)


if __name__ == '__main__':
    main()
