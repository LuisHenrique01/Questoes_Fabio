from vetor_utils import *
from matriz_utils import *
def main():
    operacao = ''
    while operacao != "S" and operacao != "M":
        operacao = input("Operação(S - Soma || M - Média): ")
    tamanho = int(input("Tamanho N: "))
    vetor = criar_vetor(tamanho)
    matriz = criar_matriz(vetor, tamanho, tamanho)
    matriz = preencher_matriz(matriz, tamanho)
    mostrar_matriz(matriz)
    if operacao == 'S':
        soma_principal = soma_ele_linha_principal(matriz)
        print("Soma dos elementos da diagonal principal = %d"%soma_principal)
        soma_secundaria = soma_ele_linha_secundaria(matriz)
        print("Soma dos elementos da diagonal secundaria = %d"%soma_secundaria)
        soma_fora = soma_ele_fora(matriz)
        print("Soma dos elementos da diagonal principal = %d"%soma_fora)
    else:
        media_principal = media_ele_linha_principal(matriz)
        print("Média dos elementos da diagonal principal = %.1f"%media_principal)
        media_secundaria = media_ele_linha_secundaria(matriz)
        print("Média dos elementos da diagonal principal = %.1f"%media_secundaria)
        media_fora = media_ele_fora(matriz)
        print("Média dos elementos da diagonal principal = %.1f"%media_fora)


def soma_ele_linha_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == i:
                soma = soma + matriz[i][j]

    return soma


def media_ele_linha_principal(matriz):
    soma = 0
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == i:
                soma = soma + matriz[i][j]
                elementos += 1

    return soma / elementos


def soma_ele_linha_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j + i == len(matriz) - 1:
                soma = soma + matriz[i][j]

    return soma


def media_ele_linha_secundaria(matriz):
    soma = 0
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j + i == len(matriz) - 1:
                soma = soma + matriz[i][j]
                elementos += 1

    return soma / elementos


def soma_ele_fora(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j + i != len(matriz) - 1 and j != i:
                soma = soma + matriz[i][j]

    return soma


def media_ele_fora(matriz):
    soma = 0
    elementos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j + i != len(matriz) - 1 and j != i:
                soma = soma + matriz[i][j]
                elementos += 1

    return soma / elementos


main()