from utils import *
def criar_arquivo(nome):
    arquivo = open(nome, "w")
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas


def abrir_arquivo(nome):
    arquivo = open(nome)
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas   


def abrir_ou_criar(nome):
    try:
        arquivo = open(nome)
    except:
        arquivo = open(nome, "w")
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas


def gravar_em_arquivo(linhas, nome):
    out = open(nome, 'w')

    for i in range(len(linhas)):
        out.write(formatar_para_arquivo(linhas[i]))
    
    out.close()
    
    
def importar_celulares(nome_arquivo):
    linhas = abrir_arquivo(nome_arquivo)

    qtd_celulares = len(linhas)
    matriz_celulares = criar_matriz(qtd_celulares, 7)
    
    for i in range(len(linhas)):
        matriz_celulares[i] = linhas[i].strip().split('#')
    return matriz_celulares
