from fabio_02a_10_dataValida import data_valida
def main():
	caracter_quebra = '/'
	data = get_data_valida('Digite uma data no formato DD/MM/AAAA (12/01/2000): ', caracter_quebra)
	dia = retorna_primeiro(data, caracter_quebra)
	mes = retorna_mes_extenso(data, caracter_quebra)
	ano = retorna_terceiro(data, caracter_quebra)

	print('%s de %s de %s'%(dia, mes, ano))


def retorna_primeiro(data, caracter_quebra):
	i = 0
	dia = ''
	while i < len(data):
		caracter = data[i]
		if caracter != caracter_quebra:
			dia = dia + caracter
		else:
			return dia
		i += 1


def retorna_segundo(data, caracter_quebra):
	i = 0
	mes = ''
	separador = 0
	while i < len(data):
		caracter = data[i]
		if caracter == caracter_quebra:
			separador += 1

		if separador == 1 and caracter != caracter_quebra:
			mes = mes + caracter
		i += 1
	return mes


def retorna_terceiro(data, caracter_quebra):
	i = 0
	ano = ''
	separador = 0
	while i < len(data):
		caracter = data[i]
		if caracter == caracter_quebra:
			separador += 1

		if separador == 2 and caracter != caracter_quebra:
			ano = ano + caracter
		i += 1
	return ano


def retorna_mes_extenso(data, caracter_quebra):
	numero_mes = int(retorna_segundo(data, caracter_quebra))
	if numero_mes == 1:
		return 'Janeiro'
	elif numero_mes == 2:
		return 'Fevereiro'
	elif numero_mes == 3:
		return 'Março'
	elif numero_mes == 4:
		return 'Abril'
	elif numero_mes == 5:
		return 'Maio'
	elif numero_mes == 6:
		return 'Junho'
	elif numero_mes == 7:
		return 'Julho'
	elif numero_mes == 8:
		return 'Agosto'
	elif numero_mes == 9:
		return 'Setembro'
	elif numero_mes == 10:
		return 'Outubro'
	elif numero_mes == 11:
		return 'Novembro'
	else:
		return 'Dezembro'


def get_data_valida(mensagem, caracter_quebra):
	data = str(input(mensagem))
	dia = int(retorna_primeiro(data, caracter_quebra))
	mes = int(retorna_segundo(data, caracter_quebra))
	ano = int(retorna_terceiro(data, caracter_quebra))

	if data_valida(dia, mes, ano) == 'Data é válida!':
		return data
	else:
		print('Digite uma data valida!!')
		return get_data_valida(mensagem, caracter_quebra)


if __name__ == '__main__':
	main()
