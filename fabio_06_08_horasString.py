from fabio_06_05_DD_MM_AAAA import retorna_primeiro, retorna_segundo, retorna_terceiro
def main():
    caracter_quebra = ':'
    horas = get_horas_validas('Digite a hora no formato(hh:mm:ss): ', caracter_quebra)
    hora = int(retorna_primeiro(horas, caracter_quebra))
    minutos = int(retorna_segundo(horas, caracter_quebra))
    segundos = int(retorna_terceiro(horas, caracter_quebra))

    print('%i hora(s), %i minuto(s) e %i segundo(s)'%(hora, minutos, segundos))


def get_horas_validas(mensagem, caracter_quebra):
    horas = str(input(mensagem))
    hora = int(retorna_primeiro(horas, caracter_quebra))
    minutos = int(retorna_segundo(horas, caracter_quebra))
    segundos = int(retorna_terceiro(horas, caracter_quebra))

    if hora <= 24 and minutos < 60 and segundos < 60:
        return horas
    else:
        print('DIGITE UMA HORA VÁLIDA!')
        return get_horas_validas(mensagem, caracter_quebra)


if __name__ == '__main__':
    main()
