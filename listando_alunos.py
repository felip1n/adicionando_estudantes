'''import json

arquivo = open('alunos.json', 'r')
alunos = json.load(arquivo)'''
alunos = []

opcoes = '1. Adicionar Aluno\n2. Remover Aluno\n3. Editar Aluno\n4. Listar Alunos\n5. Sair\nEscolha uma opção (1 a 5): '
escolha = int(input(opcoes))

while escolha != 5:
    if escolha == 1:
        nome = input('\nDigite o nome do(a) aluno(a): ')
        alunos.append(nome.upper())
        alunos.sort()
        print('\n.:. Aluno(a) adicionado(a) com sucesso! .:.\n')

    elif escolha == 2:
        nome = input('\nDigite o nome do(a) aluno(a) a remover: ')
        if nome.upper() in alunos:
            alunos.remove(nome.upper())
            print('\n.:. Aluno(a) removido(a) com sucesso! .:.\n')
        else:
            print('Aluno inexistente.')

    elif escolha == 3:
        nome = input('\nDigite o nome do(a) aluno(a) a editar: ')
        if nome.upper() in alunos:
            novo_nome = input('Digite o novo nome: ')
            pos = alunos.index(nome.upper())
            alunos[pos] = novo_nome.upper()
            print('\n.:. Aluno(a) editado(a) com sucesso! .:.\n')
        else:
            print('Aluno inexistente.')

    elif escolha == 4:
        print('\nListando os alunos:')
        pos = 0
        while pos < len(alunos):
            print('%d. %s' % (pos+1, alunos[pos]))
            pos += 1
        print()
    else:
        print('Opção inválida')

    '''arquivo = open('alunos.json', 'w')
    json.dumps(alunos, arquivo)'''

    opcoes = '\n1. Adicionar Aluno\n2. Remover Aluno\n3. Editar Aluno\n4. Listar Alunos\n5. Sair\nEscolha uma opção (1 a 5): '
    escolha = int(input(opcoes))

print('Adeus.')
