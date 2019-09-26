from vetor_utils import *
from matriz_utils import *
def main():
    tamanho = int(input("Digite o tamanho N: "))
    vetor = criar_vetor(tamanho)
    matriz = criar_matriz(vetor, tamanho, tamanho)
    matriz = preencher_matriz(matriz, tamanho)
    mostrar_matriz(matriz)
    vetor = criar_vetor(tamanho)
    matriz_transposta = criar_matriz(vetor, tamanho, tamanho)
    matriz_transposta = transposicao_matriz(matriz, matriz_transposta)
    mostrar_matriz(matriz_transposta)


def transposicao_matriz(matriz, matriz_transposta):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            a = matriz[linha][coluna]
            matriz_transposta[coluna][linha] = a
    return matriz_transposta


if __name__ == "__main__":
    main()