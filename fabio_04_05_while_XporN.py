def main():
    while True:
        x = int(input('Digite o valor de X: '))
        n = int(input('Digite o valor de N: '))
        if n > 2:
            while n > 2:
                div = x / n
                print('{:.2f} / {} = {:.2f}'.format(x, n, div))
                x = div
                n -= 1
            break
        else:
            print('Digite um numero maior que 2')


if __name__ == '__main__':
    main()
