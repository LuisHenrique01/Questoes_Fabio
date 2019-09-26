from vetor_utils import *
def main():
    tamanho = int(input("Tamanho do vetor: "))
    vetor = criar_vetor(tamanho)
    vetor = preencher_vetor_inteiros(vetor)
    printa_maior_menor(vetor)


def printa_maior_menor(vetor):
    index_menor = 0
    index_maior = 0
    maior = vetor[0]
    menor = vetor[0]
    for i in range(len(vetor)):
        if maior < vetor[i]:
            maior = vetor[i]
            index_maior = i
        if menor > vetor[i]:
            menor = vetor[i]
            index_menor = i
    print("O maior valor é V[%d] = %d"%(index_maior, maior))
    print("O menor valor é V[%d] = %d"%(index_menor, menor))


if __name__ == "__main__":
    main()