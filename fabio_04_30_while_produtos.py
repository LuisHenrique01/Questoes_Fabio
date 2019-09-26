def main():
    nome_prond = str(input('Nome do produto: '))
    while nome_prond != 'FIM':
        preco = float(input('Preço do produto: '))
        quantidade = int(input('Quantidade do produto: '))

        print('%s ---- %i = %.2f R$'%(nome_prond, quantidade, retorna_preco(preco, quantidade)))
        nome_prond = str(input('Nome do produto: '))
        

def retorna_preco(preco, quantidade):
    valor_total = preco * quantidade
    if quantidade <= 10:
        return valor_total
    elif quantidade <= 20:
        valor_total = valor_total - valor_total * 0.1
    elif quantidade <= 50:
        valor_total = valor_total - valor_total * 0.2
    else:
        valor_total = valor_total - valor_total * 0.25
    return valor_total


if __name__ == '__main__':
    main()
