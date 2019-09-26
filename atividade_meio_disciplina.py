def main():
    a = valida_entrada('Digite o valor de A: ', False)
    b = valida_entrada('Digite o valor de B: ', True)
    c = valida_entrada('Digite o valor de C: ', True)

    if delta(a, b, c) > 0 and (c != 0 and b != 0):
        print('A expressão tem duas raizes reais!')
        print('X1 = %.2f'%bhaskaraX1(a, b, c))
        print('X2 = %.2f'%bhaskaraX2(a, b, c))
    elif delta(a, b, c) == 0 or (c == 0 or b == 0):
        print('A expressão tem apenas uma raiz real!')
        if bhaskaraX1(a, b, c) != 0:
            print('X = %.2f'%bhaskaraX1(a, b, c))
        else:
            print('X = %.2f'%bhaskaraX2(a, b, c))
    else:
        print('A espreção não possui raizes reais!')


def delta(a, b, c):
    return (b**2) - (4*a*c)


def bhaskaraX1(a, b, c):
    return (b*(-1) + (delta(a, b, c)**(1/2))) / (2*a)


def bhaskaraX2(a, b, c):
    return (b*(-1) - (delta(a, b, c)**(1/2))) / (2*a)


def valida_entrada(mensagem, zerovalido):
    try:
        valor = int(input(mensagem))
        if not(zerovalido) and valor == 0:
            print('DIGITE UM A VÁLIDO!')
            return valida_entrada(mensagem, zerovalido)
        return valor
    except:
        print('DIGITE UM A VÁLIDO!')
        return valida_entrada(mensagem, zerovalido)


if __name__ == '__main__':
    main()
