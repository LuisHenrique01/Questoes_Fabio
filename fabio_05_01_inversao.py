def main():
    tamanho = int(input("Digite o tamanho: "))
    vetor_a = criar_vetor(tamanho)
    preencher_vetor_inteiros(vetor_a)
    vetor_b = criar_vetor(tamanho)
    transferir_elemento_invertidos(vetor_a, vetor_b)
    mostrar_vetor(vetor_b, "Esse é o vetor invertido!")


def transferir_elemento_invertidos(vetor_a, vetor_b):
    tm = len(vetor_a)-1
    for i in range(tm, -1, -1):
        a = vetor_a[i]
        vetor_b[tm-i] = a
    return vetor_b


def criar_vetor(tamanho_linha):
    return [0] * tamanho_linha


def preencher_vetor_inteiros(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input('V[%d] = '%i))
    return vetor


def mostrar_vetor(vetor, mensagem="Esse é o vetor!"):
    print(mensagem)
    for i in range(len(vetor)):
        print("V[%d] = %d"%(i, vetor[i]))


main()