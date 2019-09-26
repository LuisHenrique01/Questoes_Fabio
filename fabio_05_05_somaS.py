from vetor_utils import *
def main():
    vetor_a = criar_vetor(20)
    vetor_a = preencher_vetor_inteiros(vetor_a)
    soma = retorna_soma(vetor_a)
    print("A soma S: %d"%soma)


def retorna_soma(vetor):
    soma = 0
    for i in range(len(vetor)//2):
        soma += vetor[i] - vetor[19-i]
    return soma


if __name__ == "__main__":
    main()
