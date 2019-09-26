from vetor_utils import *
def main():
    tamanho = int(input("Tamanho dos vetores: "))
    vetor_a = criar_vetor(tamanho)
    vetor_b = criar_vetor(tamanho)
    inteccecao = criar_vetor(tamanho*2)
    uniao = criar_vetor(tamanho*2)
    preencher_vetor_inteiros(vetor_a)
    preencher_vetor_inteiros(vetor_b)
    inteccecao = juntar_vetores(vetor_a, vetor_b, inteccecao)
    inteccecao = retorna_repeticoes(inteccecao)
    mostrar_vetor(inteccecao, "Essa é a intesecção dos vetores!")
    uniao = juntar_vetores(vetor_a, vetor_b, uniao)
    uniao = retirar_repeticoes(uniao)
    mostrar_vetor(uniao, "Essa é a união dos vetores!")


if __name__ == "__main__":
    main()