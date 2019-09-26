from vetor_utils import *
def main():
    tamanho = int(input("Tamanho dos vetores: "))
    vetor_a = criar_vetor(tamanho)
    vetor_b = criar_vetor(tamanho)
    vetor_c = criar_vetor(tamanho*2)
    preencher_vetor_inteiros(vetor_a)
    preencher_vetor_inteiros(vetor_b)
    vetor_c = juntar_vetores(vetor_a, vetor_b, vetor_c)
    mostrar_vetor(vetor_c, "Essa é a junção dos dois vetores!")


def juntar_vetores(vetor_a, vetor_b, vetor_c):
    for i in range(len(vetor_a)):
        vetor_c[i] = vetor_a[i]
    for i in range(len(vetor_a), len(vetor_c), 1):
        vetor_c[i] = vetor_b[i-len(vetor_a)]
    return vetor_c


main()