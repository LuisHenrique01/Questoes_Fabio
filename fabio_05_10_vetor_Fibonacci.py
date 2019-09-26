from vetor_utils import *
def main():
    n = int(input("Numero de termos: "))
    vetor = criar_vetor(n)
    vetor = preencher_com_fibonacci(vetor, n)
    mostrar_vetor(vetor)

def fibonacci(n):
     if n <= 1:
         return n
     else:
         return fibonacci(n-1) + fibonacci(n-2)


def preencher_com_fibonacci(vetor, n):
    vetor_fib = []
    for i in range(1, n+1, 1):
        vetor_fib = add_apos_utimo(vetor_fib, fibonacci(i))
    return vetor_fib  


if __name__ == "__main__":
    main()