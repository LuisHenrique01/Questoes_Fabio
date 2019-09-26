def main():
    num = int(input('Digite um numero: '))
    while num > 1:
        num = num/2
    print('{:.2f}'.format(num))


if __name__ == '__main__':
        main()
