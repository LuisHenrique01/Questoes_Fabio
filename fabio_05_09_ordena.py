from vetor_utils import *
def main():
    tamanho = int(input("Tamanho do vetor: "))
    vetor = criar_vetor(tamanho)
    vetor = preencher_vetor_inteiros(vetor)
    vetor = ordena_vetor_tamanho(vetor)
    mostrar_vetor(vetor)


def ordena_vetor_tamanho(vetor):
    vetor_ord = []
    vetor_x = vetor
    for i in range(len(vetor)):
        menor = vetor[0]
        for j in range(len(vetor)):
            if menor > vetor[j]:
                menor = vetor[j]
        vetor_ord = add_apos_utimo(vetor_ord, menor)
        vetor = del_elemento_vetor(vetor, menor)
    return vetor_ord


def del_elemento_vetor(vetor, elemento):
    vetor_del = []
    cont = 0
    for i in range(len(vetor)):
        if vetor[i] != elemento or cont > 0:
            vetor_del = add_apos_utimo(vetor_del, vetor[i])
        else:
            cont += 1
    return vetor_del


if __name__ == "__main__":
    main()