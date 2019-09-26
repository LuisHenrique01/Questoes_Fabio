def transferir_elemento_invertidos(vetor_a, vetor_b):
    tm = len(vetor_a)-1
    for i in range(tm, -1, -1):
        a = vetor_a[i]
        vetor_b[tm-i] = a
    return vetor_b


def transferir_elemento(vetor_a, vetor_b):
    if len(vetor_a) > len(vetor_b):
        menor = len(vetor_b)
    else:
        menor = len(vetor_a)
    for i in range(menor):
        a = vetor_a[i]
        vetor_b[i] = a
    return vetor_b


def criar_vetor(tamanho_linha):
    return [0] * tamanho_linha


def preencher_vetor_inteiros(vetor, mensagem="__----VETOR----__"):
    print(mensagem)
    for i in range(len(vetor)):
        vetor[i] = int(input('V[%d] = '%i))
    return vetor


def mostrar_vetor(vetor, mensagem="Esse é o vetor!"):
    print(mensagem)
    for i in range(len(vetor)):
        print("V[%d] = %d"%(i, vetor[i]))


def contem_elemento_mesmo_vetor(vetor, elemento):
    cont = 0
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            cont += 1
            if cont > 1:
                return True
    return False


def contem_elemento_vetor_diferente(vetor, elemento):
    for i in range(len(vetor)):
        if vetor[i] == elemento:
            return True
    return False


def add_apos_utimo(vetor, elemento):
    new_vetor = criar_vetor(len(vetor)+1)
    transferir_elemento(vetor, new_vetor)
    new_vetor[len(new_vetor)-1] = elemento
    return new_vetor


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


def retorna_repeticoes(vetor):
    vetor_sem_rep = []
    for i in range(len(vetor)):
        if contem_elemento_mesmo_vetor(vetor, vetor[i]) and not contem_elemento_vetor_diferente(vetor_sem_rep, vetor[i]):
            vetor_sem_rep = add_apos_utimo(vetor_sem_rep, vetor[i]) 
    return vetor_sem_rep


def retirar_repeticoes(vetor):
    vetor_sem_rep = []
    for i in range(len(vetor)):
        if contem_elemento_mesmo_vetor(vetor, vetor[i]) and not contem_elemento_vetor_diferente(vetor_sem_rep, vetor[i]):
            vetor_sem_rep = add_apos_utimo(vetor_sem_rep, vetor[i]) 
        if not contem_elemento_mesmo_vetor(vetor, vetor[i]):
            vetor_sem_rep = add_apos_utimo(vetor_sem_rep, vetor[i])          
    return vetor_sem_rep



def juntar_vetores(vetor_a, vetor_b, vetor_c):
    for i in range(len(vetor_a)):
        vetor_c[i] = vetor_a[i]
    for i in range(len(vetor_a), len(vetor_c), 1):
        vetor_c[i] = vetor_b[i-len(vetor_a)]
    return vetor_c


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