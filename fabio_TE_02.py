def main():
    vetor = [int(input('Digite um numero: ')) for i in range(3)]
    em_ordem = sorted(vetor)
    for i in range(3):print('%dº = %d'%(i+1, em_ordem[i]))


if __name__ == "__main__":
    main()
