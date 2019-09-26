def main():
    numero = int(input("Numero de até 3 digitos: "))
    print('O numero em romano é: %s'%mil_romano(numero))


def mil_romano(numero):
    numero_romano = (numero // 1000) * 'M'
    numero_romano_final = numero_romano + novecentos_romano(numero % 1000)
    return numero_romano_final


def novecentos_romano(numero):
    numero_romano = (numero // 900) * 'CM'
    numero_romano_final = numero_romano + quinhentos_romano(numero % 900)
    return numero_romano_final


def quinhentos_romano(numero):
    numero_romano = (numero // 500) * 'D'
    numero_romano_final = numero_romano + quatrocentos_romano(numero % 500)
    return numero_romano_final


def quatrocentos_romano(numero):
    numero_romano = (numero // 400) * 'CD'
    numero_romano_final = numero_romano + cem_romano(numero % 400)
    return numero_romano_final


def cem_romano(numero):
    numero_romano = (numero // 100) * 'C'
    numero_romano_final = numero_romano + noventa_romano(numero % 100)
    return numero_romano_final


def noventa_romano(numero):
    numero_romano = (numero // 90) * 'XC'
    numero_romano_final = numero_romano + ciquenta_romano(numero % 90)
    return numero_romano_final


def ciquenta_romano(numero):
    numero_romano = (numero // 50) * 'L'
    numero_romano_final = numero_romano + quanrenta_romano(numero % 50)
    return numero_romano_final


def quanrenta_romano(numero):
    numero_romano = (numero // 40) * 'XL'
    numero_romano_final = numero_romano + dez_romano(numero % 40)
    return numero_romano_final


def dez_romano(numero):
    numero_romano = (numero // 10) * 'X'
    numero_romano_final = numero_romano + nove_romano(numero % 10)
    return numero_romano_final


def nove_romano(numero):
    numero_romano = (numero // 9) * 'IX'
    numero_romano_final = numero_romano + cinco_romano(numero % 9)
    return numero_romano_final


def cinco_romano(numero):
    numero_romano = (numero // 5) * 'V'
    numero_romano_final = numero_romano + quatro_romano(numero % 5)
    return numero_romano_final


def quatro_romano(numero):
    numero_romano = (numero // 4) * 'IV'
    numero_romano_final = numero_romano + um_romano(numero % 4)
    return numero_romano_final


def um_romano(numero):
    numero_romano = (numero // 1) * 'I'
    return numero_romano


if __name__ == '__main__':
    main()
