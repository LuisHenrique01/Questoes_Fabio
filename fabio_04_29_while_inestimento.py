def main():
    novo = 'S'
    anos = 1
    valor_anual = 0
    investimento = int(input('Valor do investimento mensal: '))
    taxa = int(input('Valor da taxa(em %): '))
    while novo == 'S':
        rendimento = retorno_anual(investimento, taxa, valor_anual)
        print('Com %i ano(s) você terá um retorno de %.2f R$'%(anos, rendimento))
        novo = str(input('Deseja calcular novo ano(S - sim N - Não)? '))
        anos += 1
        valor_anual = rendimento

def retorno_anual(investimento_fixo, taxa, valor_anual):
    i = 1
    investimento = investimento_fixo + valor_anual
    while i < 12:
        valor_anual = investimento + investimento * (taxa / 100)
        investimento = investimento_fixo + valor_anual
        i += 1
    return valor_anual + investimento_fixo

if __name__ == '__main__':
    main()
