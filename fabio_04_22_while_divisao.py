def main():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))
    if a > b:
        print('%i / %i = %s' %(a, b, divisao(a, b)))
    else:
        print('%i / %i = %s' %(b, a, divisao(b, a)))



def divisao(a, b):
    div = 0
    while (a - b) >= 0:
        a -= b
        div += 1
    return '%i \nresto = %i'%(div, a)


if __name__ == '__main__':
    main()
