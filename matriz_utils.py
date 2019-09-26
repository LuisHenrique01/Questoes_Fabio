def preencher_matriz(matriz, tamanho_linha):
    for i in range(len(matriz)):
        matriz[i] = preencher_vetor_inteiros(criar_vetor(tamanho_linha), "M[%d]"%i)
    return matriz

def criar_matriz(vetor, numero_linhas, tamanho_linha):
    matriz = [vetor]*numero_linhas
    for i in range(len(matriz)):
        matriz[i] = criar_vetor(tamanho_linha)
    return matriz


def criar_vetor(tamanho_linha):
    return [0]*tamanho_linha


def preencher_vetor_inteiros(vetor, mensagem="M"):
    for i in range(len(vetor)):
        vetor[i] = int(input('%s[%d] = '%(mensagem, i)))
    return vetor


def soma_ele_linha(matriz, linha):
    soma = 0
    for i in range(len(matriz[linha])):
        soma += matriz[linha][i]
    return soma


def mutiplica_ele_linha(matriz, linha):
    soma = 0
    for i in range(len(matriz[linha])):
        soma *= matriz[linha][i]
    return soma



def soma_ele_linha(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i and j + i > len(matriz) - 1:
                soma = soma + matriz[i][j]

    return soma


def media_ele_linha(matriz):
    soma = 0
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i and j + i > len(matriz) - 1:
                soma = soma + matriz[i][j]
                elementos += 1

    return soma / elementos


def mostrar_matriz(matriz, msg="Essa é a matriz!"):
    print(msg)
    for i in range(len(matriz)):
        print(" ", end = ' ')
        for j in range(len(matriz[i])):
            if j != len(matriz[i]) - 1:
                print("%d"%matriz[i][j], end = '   ')
            else:
                print("%d"%matriz[i][j])


def transposicao_matriz(matriz, matriz_transposta):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            a = matriz[linha][coluna]
            matriz_transposta[coluna][linha] = a
    return matriz_transposta
