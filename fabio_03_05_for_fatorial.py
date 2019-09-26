def main():
    num = int(input('Digite um numero: '))
    if num > 0:
        print('Fotorial = %i'%(fatorial(num)))
    elif num == 0:
        print('Fatorial = 1')
    else:
        print('DIGITE UM NUMERO POSITIVO!')
        main()


def fatorial(num):
    fat = 1
    for i in range(1, num+1):
        fat *= i
    return fat

if __name__ == '__main__':
    main()