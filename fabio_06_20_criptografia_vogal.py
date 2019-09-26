from ferramentas_STRING_python import e_vogal
def main():
    texto = str(input('texto: '))
    print('Texto criptografado: %s'%criptorgia(texto))
    print('Texto descriptografado: %s'%revertendo_criptografia(texto))

def criptorgia(texto):
    i = 0
    new_texto = ''
    while i < len(texto):
        if not(e_vogal(texto[i])):
            new_texto = new_texto + texto[i]
        i += 1
    return new_texto


def revertendo_criptografia(texto):
    i = 0 #Contador 1º while
    j = 0 #Contador 2º while
    k = 0 # Contador vogais e posicao
    new_texto = ''
    vogais = ''
    posicao = ''
    while i < len(texto):
        if e_vogal(texto[i]):
            vogais = vogais + texto[i]
            posicao = posicao + str(i)
        i += 1

    while j < len(texto):
        if j == int(posicao[k]):
            new_texto = new_texto + vogais[k]
            k += 1
        else:
            new_texto = new_texto + texto[j]
        j += 1

    return new_texto


if __name__ == '__main__':
    main()
