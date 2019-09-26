def main():
    distancia = int(input('Distancia entre as cidades(Km): '))
    tanque = int(input('Litros de combustivel no tanque(Litros): '))
    distancia_percorrida = int(input('Distância percorrida desde a última medição: '))
    litros_usados_percorrido = int(input('Quantidade de litros consumidos para percorrer a distância indicada: '))

    print(chegou_no_destino(distancia, tanque, distancia_percorrida, litros_usados_percorrido))
    print('O consumo foi de %.2f Km/L' % consumo(distancia_percorrida, litros_usados_percorrido))

def consumo(distancia_percorrida, litros_usados_percorrido):
    return distancia_percorrida / litros_usados_percorrido


def chegou_no_destino(distancia, tanque, distancia_percorrida, litros_usados_percorrido):
    if litros_usados(distancia, distancia_percorrida, litros_usados_percorrido) <= tanque:
        return 'O carro chegou no destino final!'
    else:
        return 'O carro não conseguiu chegar no destino por falta de combustivel! Faltou %i litros' %litros_usados(distancia, distancia_percorrida, litros_usados_percorrido) - tanque


def litros_usados(distancia, distancia_percorrida, litros_usados_percorrido):
    while distancia > distancia_percorrida:
        distancia_percorrida += distancia_percorrida
        litros_usados_percorrido += litros_usados_percorrido
    return litros_usados_percorrido


if __name__ == '__main__':
    main()
