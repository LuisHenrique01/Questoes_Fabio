from vetor_utils import *
def main():
    tamanho = int(input("Tamanho do vetor: "))
    vetor = criar_vetor(tamanho)
    preencher_vetor_inteiros(vetor)
    vetor_rep = elementos_repetidos(vetor)
    vetor_sem_rep = retirar_repeticoes(vetor_rep)
    mostrar_vetor(vetor_sem_rep, "Este é um vetor só com elementos repetidos!")


def elementos_repetidos(vetor):
    vetor_rep = []
    cont = 0
    index = 0
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if vetor[i] == vetor[j] and i != j:
                vetor_rep = add_apos_utimo(vetor_rep, vetor[i])
                cont += 1
    return vetor_rep


def retirar_repeticoes(vetor):
    vetor_sem_rep = []
    for i in range(len(vetor)):
        if contem_elemento(vetor, vetor[i]) and not contem_elemento_novos(vetor_sem_rep, vetor[i]):
            vetor_sem_rep = add_apos_utimo(vetor_sem_rep, vetor[i]) 
    return vetor_sem_rep


def contem_elemento(vetor, elemento):
    cont = 0
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            cont += 1
            if cont > 1:
                return True
    return False


def contem_elemento_novos(vetor, elemento):
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            return True
    return False


def add_apos_utimo(vetor, elemento):
    new_vetor = criar_vetor(len(vetor)+1)
    transferir_elemento(vetor, new_vetor)
    new_vetor[len(new_vetor)-1] = elemento
    return new_vetor


main()