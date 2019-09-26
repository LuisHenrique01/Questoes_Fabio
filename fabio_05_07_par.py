from vetor_utils import *
def main():
    # vetor_a = [int(input("V[%d] = "%i)) for i in range(int(input("Tamanho do vetor: ")))]
    # vetor_b = [0 if vetor_a[i] % 2 == 0 else 1 for i in range(len(vetor_a))]
    # for i in range(len(vetor_a)): print("V_B[%d] = %d"%(i, vetor_b[i]))

    vetor_a = criar_vetor(8)
    vetor_a = preencher_vetor_inteiros(vetor_a)
    vetor_b = criar_vetor(8)
    vetor_b = valores_substituidos(vetor_a, vetor_b)
    mostrar_vetor(vetor_b)


def valores_substituidos(vetor_a, vetor_b):
    for i in range(len(vetor_a)):
        if vetor_a[i] % 2 == 0:
            vetor_b[i] = 0
        else:
            vetor_b[i] = 1
    return vetor_b

if __name__ == "__main__":
    main()
