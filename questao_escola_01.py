def main():
    #DADOS INICIAIS DOS ALUNOS
    aluno_01 = ['Luis', 'Módulo 1', 'Calculo 1', 10, 7, 8]
    aluno_02 = ['Marcos', 'Módulo 1', 'Calculo 1', 9, 7, 5]
    aluno_03 = ['Maria', 'Módulo 1', 'Calculo 1', 2, 4, 3]
    aluno_04 = ['Fernanda', 'Módulo 2', 'Calculo 2', 5, 10, 8]
    aluno_05 = ['Luiza', 'Módulo 2', 'Calculo 2', 8, 7, 2]
    aluno_06 = ['Léticia', 'Módulo 2', 'Calculo 2', 7, 7, 8]
    #DADOS DO SISTEMA QUE SERÃO UTILIZADOS
    dados_escola = ['UFPI','Bairro - Ininga, Teresina - PI','(86) 3215-5513', 'ufpi@gmail.com']
    todos_alunos = [aluno_01, aluno_02, aluno_03, aluno_04, aluno_05, aluno_06]
    dados_turma1 = [aluno_01, aluno_02, aluno_03]
    dados_turma2 = [aluno_04, aluno_05, aluno_06]
    dados_disciplina1 = [aluno_01, aluno_02, aluno_03]
    dados_disciplina2 = [aluno_04, aluno_05, aluno_06]
    opcao = 0
    while opcao != 5:
        print('-'*19,'ESCOLA','-'*19)
        opcao = valida_entrada('1 - Dados da escola\n2 - Dados das turmas\n3 - Dados das disciplinas\n4 - Dados dos alunos\n5 - Sair\n')
        if opcao == 1:
            #print('Digite os novos dados conforme os atuais!')
            dados_escola = att_dados_escola(dados_escola)
            print('-'*15,' NOVOS DADOS ','-'*15)
            print('NOME:    ',dados_escola[0])
            print('ENDEREÇO:',dados_escola[1])
            print('NUMERO:  ',dados_escola[2])
            print('E-MAIL:  ',dados_escola[3])
        elif opcao == 2:
            print('-'*15,' TURMAS ','-'*15)
            turma = valida_entrada('1 - "Módulo 1"\n2 - "Módulo 2"\n', 2)
            if turma == 1:
                imprimir_dados_turma(dados_turma1)
            else:
                imprimir_dados_turma(dados_turma2)
        elif opcao == 3:
            print('-'*15,' disciplina '.upper(),'-'*15)
            turma = valida_entrada('1 - "Calculo 1"\n2 - "Calculo 2"\n', 2)
            if turma == 1:
                imprimir_dados_disciplina(dados_disciplina1)
            else:
                imprimir_dados_disciplina(dados_disciplina2)
        elif opcao == 4:
            todos_alunos = att_dados_alunos(todos_alunos)
            print('-'*8,'DADOS DE TODOS OS ALUNOS ATUALIZADOS','-'*8)
            i = 0
            j = 0
            while i < len(todos_alunos):
                while j < len(todos_alunos[i]):
                    if j == 0:
                        print('NOME      :',todos_alunos[i][j])
                    elif j == 1:
                        print('TURMA     :',todos_alunos[i][j])
                    elif j == 2:
                        print('DISCIPLINA:',todos_alunos[i][j])
                    else:
                        print('NOTA      :',todos_alunos[i][j])
                    j += 1
                print('-'*46)
                i += 1
                j = 0


def att_dados_alunos(todos_alunos):
    i = 0
    mais_alunos = 1
    print('-'*15,' ALUNOS ','-'*15)
    while i < len(todos_alunos):
        print(i+1,'-', todos_alunos[i][0])
        i += 1
    while mais_alunos == 1:
        att_dado_exato(todos_alunos, i)
        mais_alunos = valida_entrada('DESEJA ALTERAR DADOS DE OUTRO AULO?(1 - SIM | 2 - NÃO)? ', 2)
    return todos_alunos

def att_dado_exato(todos_alunos, i):
    outro_dado = 1
    while outro_dado == 1:
        aluno = valida_entrada('ESCOLHA UM ALUNO: ', i) - 1
        print('-'*30)
        print('1 - NOME   :',todos_alunos[aluno][0])
        print('2 - TURMA  :',todos_alunos[aluno][1])
        print('3 - MATERIA:',todos_alunos[aluno][2])
        print('4 - NOTAS  :',todos_alunos[aluno][3], todos_alunos[aluno][4], todos_alunos[aluno][5])
        print('5 - SAIR')
        dado = valida_entrada('ESCOLHA O ITEM A SER ATUALIZADO: ',5) - 1
        if dado == 4:
            return todos_alunos
        elif dado == 3:
            todos_alunos[aluno][dado] = int(input('NOVAS NOTAS: '))
            todos_alunos[aluno][dado+1] = int(input('NOVAS NOTAS: '))
            todos_alunos[aluno][dado+2] = int(input('NOVAS NOTAS: '))
        else:
            todos_alunos[aluno][dado] = str(input('NOVO DADO: '))
        outro_dado = valida_entrada('DESEJA ALTERAR OUTRO DADO(1 - SIM | 2 - NÃO)? ', 2)
    return todos_alunos


def att_dados_escola(dados_escola):
    print('-'*15,'DADOS ATUAIS','-'*15)
    print('NOME:    ',dados_escola[0])
    print('ENDEREÇO:',dados_escola[1])
    print('NUMERO:  ',dados_escola[2])
    print('E-MAIL:  ',dados_escola[3])
    print('1 - NOME | 2 - ENDEREÇO | 3 - NUMERO | 4 - MAIL | 5 - SAIR')
    i = valida_entrada()
    while i != 5:
        dados_escola[i-1] = input('NOVO DADO: ')
        i = valida_entrada('NOVA OPÇÃO: ')
    return dados_escola


def imprimir_dados_disciplina(dados_disciplina1):
    i = 0
    media_turma = 0
    maior_media = -1
    menor_media = 11
    while i < len(dados_disciplina1):
            media = (dados_disciplina1[i][3] + dados_disciplina1[i][4] + dados_disciplina1[i][5])/3
            if media > maior_media:
                maior_media = media
            elif media < menor_media:
                menor_media = media
            media_turma += media
            i += 1
    media_turma = media_turma / i+1
    print('-'*15, 'DADOS', '-'*15)
    print('MEDIA DA TURMA = %.2f'%media_turma)
    print('MAIOR MEDIA    = %.2f'%maior_media)
    print('MENOR MEDIA    = %.2f'%menor_media)
    return


def imprimir_dados_turma(dados_turma):
    i = 0
    print('-'*15,'ALUNOS','-'*15)
    while i < len(dados_turma):
        print(dados_turma[i][0])
        i += 1
    return


def valida_entrada(mensagem='DIGITE A OPÇÃO: ', numero_opcao=5):
    opcao = str(input(mensagem.upper()))
    if int(opcao) <= numero_opcao:
        return int(opcao)
    else:
        print('DIGITE UM VALOR VÁLIDO!')
        return valida_entrada(mensagem, numero_opcao)


if __name__ == '__main__':
    main()
