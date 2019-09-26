def main():
    container = int(input('Numero de container: '))
    pesoContainer = 0
    pesoBagagem = 0
    pesoPesoas = 0
    quantidadePasa = 0
    cont = 1
    while cont <= container:
        pesoContainer += int(input('Peso de cada container: '))
        cont += 1

    while True:
        bilhete = int(input('Numero de bilhete: '))
        if bilhete == 0:
            break
        else:
            pesoBagagem += int(input('Quantidade de bagagens: ')) * 10
            pesoPesoas += 70
            quantidadePasa += 1

    print('Quantidade de passageiros: {}'.format(quantidadePasa))
    print('Quantidade total volume da bagagem: {}'.format(pesoBagagem))
    print('Peso dos passageiros: {}'.format(pesoPesoas))
    print('Volume da carga: {}'.format(pesoContainer))
    print('Quantidade posivel de combustivel: {:.2f}'.format(quantidadeDeCombustivel(pesoContainer, pesoBagagem, pesoPesoas, quantidadePasa)))
    print(pode_decolar(pesoContainer, pesoBagagem, pesoPesoas, quantidadePasa))


def quantidadeDeCombustivel(pesoContainer, pesoBagagem, pesoPesoas, quantidadePasa):
    pesoTotal = pesoPesoas + pesoBagagem + pesoContainer
    combustivel = (500000 - pesoTotal) / 1.5
    return combustivel


def pode_decolar(pesoContainer, pesoBagagem, pesoPesoas, quantidadePasa):
    if quantidadeDeCombustivel(pesoContainer, pesoBagagem, pesoPesoas, quantidadePasa) >= 100001:
        return 'O AVIÃO PODE DECOLOLAR!!!'
    else:
        return 'O AVIÃO NÃO PODE DECOLOLAR!!!'


if __name__ == '__main__':
    main()
