def main():
    #Alunos
    aluno1 = ['Irui', '4311','Historia', 7, 7 , 0]
    aluno2 = ['Edsonyse', '4311','Historia', 6, 10 , 10]
    aluno3 = ['Macivan', '4411','Biologia', 4, 5 , 9]
    aluno4 = ['Matheus', '4411','Biologia', 6, 5 , 8]
    #Escola
    escola = ['IFPI', 'R. Álvaro Mendes', 'Teresina - PI', '(86) 3215-5200']
    #disciplina
    disciplinas = ['Historia', 'Biologia']
    #turmas
    turmas = ['4311', '4411']
    while True:
        print('DIGITE O NUMERO CORRESPONDENTE A OPERAÇÃO')
        print('(1) Dados da escola\n(2) Dados das turmas\n(3) Dados das disciplinas\n(4) Dados dos alunos\n(5) Sair')
        menu = int(entrada(5, 1))

        if menu == 1:
            print('Dados da escola')
            print('(1) Nome : %s \n(2) Rua  : %s\n(3) Cidade: %s\n(4) Número: %s\n(5) Sair'%(escola[0], escola[1], escola[2], escola[3]))
            alt_escola = int(entrada(5, 1)) - 1
            if alt_escola == 0:
                escola[alt_escola] = str(input('Atualização: '))
            elif alt_escola == 1:
                escola[alt_escola] = str(input('Atualização: '))
            elif alt_escola == 2:
                escola[alt_escola] = str(input('Atualização: '))
            elif alt_escola == 3:
                escola[alt_escola] = str(input('Atualização: '))
            #Não precisa do esle
            if alt_escola != 5:#print só caso tenha alteração
                print('Novos dados da escola')
                print('(1) Nome : %s \n(2) Rua  : %s\n(3) Cidade: %s\n(4) Número: %s\n(5) Sair'%(escola[0], escola[1], escola[2], escola[3]))
        elif menu == 2:
            print('Tumas:\n(1) 4311\n(2) 4411')
            turma = entrada(2, 1)
            if turma == 1:
                if aluno1[1] == '4311':
                    print(aluno1[0])
                if aluno2[1] == '4311':
                    print(aluno2[0])
                if aluno3[1] == '4311':
                    print(aluno3[0])
                if aluno4[1] == '4311':
                    print(aluno4[0])
            else:
                if aluno1[1] == '4411':
                    print(aluno1[0])
                if aluno2[1] == '4411':
                    print(aluno2[0])
                if aluno3[1] == '4411':
                    print(aluno3[0])
                if aluno4[1] == '4411':
                    print(aluno4[0])
        elif menu == 3:
            print('Dados das disciplinas')
            print('Tumas:\n(1) Historia\n(2) Biologia')
            disciplina = entrada(2, 1)
            if disciplina == 1:
                print('--Historia--')
                media_geral = (((aluno1[3]+aluno1[4]+aluno1[5])/3) + ((aluno2[3]+aluno2[4]+aluno2[5])/3)) / 2
                media1 = (aluno1[3]+aluno1[4]+aluno1[5])/3
                media2 = (aluno2[3]+aluno2[4]+aluno2[5])/3
                print('Media geral: %.2f'%media_geral)
                if media1 > media2:
                    print('Menor media: %.2f'%media2)
                    print('Maior media: %.2f'%media1)
                else:
                    print('Menor media: %.2f'%media1)
                    print('Maior media: %.2f'%media2)
            else:
                print('--Biologia--')
                media_geral = (((aluno3[3]+aluno3[4]+aluno3[5])/3) + ((aluno4[3]+aluno4[4]+aluno4[5])/3)) / 2
                media1 = (aluno3[3]+aluno3[4]+aluno3[5])/3
                media2 = (aluno4[3]+aluno4[4]+aluno4[5])/3
                print('Media geral: %.2f'%media_geral)
                if media1 > media2:
                    print('Menor media: %.2f'%media2)
                    print('Maior media: %.2f'%media1)
                else:
                    print('Menor media: %.2f'%media1)
                    print('Maior media: %.2f'%media2)
        elif menu == 4:
            print('Selecione um aluno')
            print('(1)',aluno1[0])
            print('(2)',aluno2[0])
            print('(3)',aluno3[0])
            print('(4)',aluno4[0])
            aluno = entrada(4, 1)
            if aluno == 1:
                print('='*10)
                print('Nome:',aluno1[0])
                print('Turma:',aluno1[1])
                print('Disciplina:',aluno1[2])
                print('Notas:',aluno1[3], aluno1[4], aluno1[5])
                print('====== Atualização =====')
                aluno1[0] = str(input('Nome: '))
                aluno1[1] = str(input('Turma: '))
                aluno1[2] = str(input('Disciplina: '))
                aluno1[3], aluno1[4], aluno1[5] = map(int, input('Notas(Separadas por um espaço): ').split(' '))
                print('===== Novos dados =====')
                print('Nome:',aluno1[0])
                print('Turma:',aluno1[1])
                print('Disciplina:',aluno1[2])
                print('Notas:',aluno1[3], aluno1[4], aluno1[5])
            elif aluno == 2:
                print('='*10)
                print('Nome:',aluno2[0])
                print('Turma:',aluno2[1])
                print('Disciplina:',aluno2[2])
                print('Notas:',aluno2[3], aluno2[4], aluno2[5])
                print('====== Atualização =====')
                aluno2[0] = str(input('Nome: '))
                aluno2[1] = str(input('Turma: '))
                aluno2[2] = str(input('Disciplina: '))
                aluno2[3], aluno2[4], aluno2[5] = map(int, input('Notas(Separadas por um espaço): ').split(' '))
                print('===== Novos dados =====')
                print('Nome:',aluno2[0])
                print('Turma:',aluno2[1])
                print('Disciplina:',aluno2[2])
                print('Notas:',aluno2[3], aluno2[4], aluno2[5])
            elif aluno == 3:
                print('='*10)
                print('Nome:',aluno3[0])
                print('Turma:',aluno3[1])
                print('Disciplina:',aluno3[2])
                print('Notas:',aluno3[3], aluno3[4], aluno3[5])
                print('====== Atualização =====')
                aluno3[0] = str(input('Nome: '))
                aluno3[1] = str(input('Turma: '))
                aluno3[2] = str(input('Disciplina: '))
                aluno3[3], aluno3[4], aluno3[5] = map(int, input('Notas(Separadas por um espaço): ').split(' '))
                print('===== Novos dados =====')
                print('Nome:',aluno3[0])
                print('Turma:',aluno3[1])
                print('Disciplina:',aluno3[2])
                print('Notas:',aluno3[3], aluno3[4], aluno3[5])
            else:
                print('='*10)
                print('Nome:',aluno4[0])
                print('Turma:',aluno4[1])
                print('Disciplina:',aluno4[2])
                print('Notas:',aluno4[3], aluno4[4], aluno4[5])
                print('====== Atualização =====')
                aluno4[0] = str(input('Nome: '))
                aluno4[1] = str(input('Turma: '))
                aluno4[2] = str(input('Disciplina: '))
                aluno4[3], aluno4[4], aluno4[5] = map(int, input('Notas(Separadas por um espaço): ').split(' '))
                print('===== Novos dados =====')
                print('Nome:',aluno4[0])
                print('Turma:',aluno4[1])
                print('Disciplina:',aluno4[2])
                print('Notas:',aluno4[3], aluno4[4], aluno4[5])
        else:
            break


def entrada(entradamaior, entradamenor):
    try:
        menu = int(input())
        if menu >= entradamenor and menu <= entradamaior:
            return menu
        else:
            print('DIGITE UM VALOR PRESENTE NO MENU!')
            return entrada(entradamaior, entradamenor)
    except Exception:
        print('DIGITE UM VALOR INTEIRO!')
        return entrada(entradamaior, entradamenor)


if __name__ == '__main__':
    main()
