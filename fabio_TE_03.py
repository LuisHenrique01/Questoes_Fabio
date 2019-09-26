def main():
    vetor = [int(input('Digite um ângulo: ')) for i in range(3)]
    if 0 in vetor or sum(vetor) != 180:
        print('Não forma um triângulo!')
    else:
        if 90 in vetor:
            print('Triângulo retângulo')
        elif max(vetor) < 90: 
            print('Triângulo acutângulo')
        elif max(vetor) > 90:
            print('Triângulo obtusângulo')


if __name__ == "__main__":
    main()