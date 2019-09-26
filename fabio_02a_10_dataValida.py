def ebixeto(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True
    elif ano % 400 == 0:
        return True
    else:
        return False

def data_valida(dia, mes, ano):
    if ebixeto(ano):
        if mes == 1:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data inválida!")
        elif mes == 2:
            if dia <= 29:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 3:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 4:
            if dia <= 30:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 5:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 6:
            if dia <= 30:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 7:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 8:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 9:
            if dia <= 30:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 10:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 11:
            if dia <= 30:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 12:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        else:
            return("Data é inválida!")
    else:
        if mes == 1:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data inválida!")
        elif mes == 2:
            if dia <= 28:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 3:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 4:
            if dia <= 30:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 5:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 6:
            if dia <= 30:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 7:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 8:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 9:
            if dia <= 30:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 10:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 11:
            if dia <= 30:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        elif mes == 12:
            if dia <= 31:
                return("Data é válida!")
            else:
                return("Data é inválida!")
        else:
            return("Data é inválida!")

def main():
    lista = input("Digite a data deseja verificar:\n").split(' ')

    dia = int(lista[0])
    mes = int(lista[1])
    ano = int(lista[2])

    print(data_valida(dia, mes, ano))

if __name__ == '__main__':
    main()
