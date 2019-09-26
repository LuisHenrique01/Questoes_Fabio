from arquivo_utils import *
def contem(registro, chave, valor):
    #As linhas seram as chaves no meu caso
    for j in range(len(registro)):
        if registro[j][chave]  == valor:
            return True
    return False


def filtra(dados, chave, valor):
    #As linhas seram as chaves no meu caso 
    vetor = []
    for j in range(len(dados)):
        if dados[j][chave] == valor:
            vetor = add_apos_utimo(vetor, j)
    return vetor


def media(dados, chave):
    soma = 0
    elementos = 0
    for j in range(len(dados)):
        soma += int(dados[j][chave])
        elementos += 1
    return soma / elementos


def maior(dados, chave):
    maior = int(dados[0][chave])
    for j in range(len(dados)):
        if maior < int(dados[j][chave]):
            maior = int(dados[j][chave])
    return maior


def menor(dados, chave):
    menor = int(dados[0][chave])
    for j in range(len(dados)):
        if menor > int(dados[j][chave]):
            menor = int(dados[j][chave])
    return menor


def menu():
    menu = '******** App celulares ********' \
        + '\n1 - Novo celular' \
        + '\n2 - Listar celulares' \
        + '\n3 - Filtros' \
        + '\n4 - Média de todos os celulares' \
        + '\n5 - Média de uma marca' \
        + '\n6 - Celular mais barato e mais caro' \
        + '\n7 - Melhor custo benefício' \
        + '\n0 - Sair' \
        + '\n\nopcao >> '
    return get_opcao(menu, 0, 7)


def add_apos_utimo(vetor, elemento):
    new_vetor = criar_vetor(len(vetor)+1)
    transferir_elemento(vetor, new_vetor)
    new_vetor[len(new_vetor)-1] = elemento
    return new_vetor


def criar_vetor(tamanho_linha=0):
    return [0]*tamanho_linha


def criar_matriz(numero_linhas=0, tamanho_linha=0):
    matriz = [0]*numero_linhas
    for i in range(len(matriz)):
        matriz[i] = criar_vetor(tamanho_linha)
    return matriz


def transferir_elemento(vetor_a, vetor_b):
    if len(vetor_a) > len(vetor_b):
        menor = len(vetor_b)
    else:
        menor = len(vetor_a)
    for i in range(menor):
        a = vetor_a[i]
        vetor_b[i] = a
    return vetor_b


def mostrar_todos_celulares(celulares):
    print()
    for i in range(len(celulares)):
        print("++++++++++++++++++++++++++++++++++++++++++++++")
        print("Fabricante: %s"%celulares[i][0])
        print("Modelo: %s"%celulares[i][1])
        print("Sistema operacional(SO): %s"%celulares[i][2])
        print("Memoria RAM: %s GB"%celulares[i][3])
        print("Memoria interna: %s GB"%celulares[i][4])
        print("Frequencia do processador: %s GHz"%celulares[i][5])
        print("Preço médio: %s R$"%celulares[i][6])
        print()


def get_opcao(mensagem='Deseja continuar(0 - SIM || 1 - NÃO)', v_min=0, v_max=1):
    op = int(input(mensagem))
    if op >= v_min and op <= v_max:
        return op
    else:
        return get_opcao(mensagem, v_min, v_max)


def mostrar_celulares_por_dois_filtros(celulares, index_filtro1, index_filtro2, filtro1, filtro2):
    print()
    tem = 0
    for i in range(len(celulares)):
        if celulares[i][index_filtro1].upper() == filtro1.upper() and celulares[i][index_filtro2].upper() == filtro2.upper():
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            print("Fabricante: %s"%celulares[i][0])
            print("Modelo: %s"%celulares[i][1])
            print("Sistema operacional(SO): %s"%celulares[i][2])
            print("Memoria RAM: %s GB"%celulares[i][3])
            print("Memoria interna: %s GB"%celulares[i][4])
            print("Frequencia do processador: %s GHz"%celulares[i][5])
            print("Preço médio: %s R$"%celulares[i][6])
            print()
            tem = 1
    if tem == 0:
        print("Não temos com essas especificações!")
    

def mostrar_celulares_por_um_filtros(celulares, index_filtro, filtro, mostrar=True):
    print()
    celulares_filtrados = []
    tem = 0
    for i in range(len(celulares)):
        if celulares[i][index_filtro].upper() == filtro.upper():
            if mostrar:
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print("Fabricante: %s"%celulares[i][0])
                print("Modelo: %s"%celulares[i][1])
                print("Sistema operacional(SO): %s"%celulares[i][2])
                print("Memoria RAM: %s GB"%celulares[i][3])
                print("Memoria interna: %s GB"%celulares[i][4])
                print("Frequencia do processador: %s GHz"%celulares[i][5])
                print("Preço médio: %s R$"%celulares[i][6])
                print()
            celulares_filtrados = add_apos_utimo(celulares_filtrados, celulares[i])
            tem = 1
    if tem == 0:
        print("Não temos com essas especificações!")
    return celulares_filtrados


def custo_beneficio(celulares, ram, interna, ghz, preco):
    # Soma dos atributos menos o preco mutiplicado por 100, vai resultar no preço medio do produto desejado
    pesos = ((ram + interna + ghz) - preco)*100
    melhor = 0
    menor = float(celulares[0][6]) - pesos
    for i in range(len(celulares)):
        if float(celulares[i][6]) - pesos < menor:
            menor = float(celulares[i][6])
            melhor = i
    
    melhor_modelo = celulares[melhor][1]

    return melhor_modelo


def formatar_para_arquivo(celular):
    return '%s#%s#%s#%s#%s#%s#%s\n'%(str(celular[0]), str(celular[1]), str(celular[2]), str(celular[3]), str(celular[4]), str(celular[5]), str(celular[6]))
