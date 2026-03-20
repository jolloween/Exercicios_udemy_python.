import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


tarefas = []
desfeitas = []

while True:
    limpar_tela()
    print('comandos: listar, desfazer, refazer: ')
    opcao = input('Digite uma tarefa ou comando: ').lower()

    if opcao == 'listar':
        if not tarefas:
            print('não tem tarefas.')

        for t in tarefas:
            print(t)
        input('\nPress enter to exit...')

    elif opcao == 'desfazer':
        if tarefas:
            desfazer_ultima_tarefa = tarefas.pop()
            desfeitas.append(desfazer_ultima_tarefa)
            print(f'tarefa desfeita: {desfazer_ultima_tarefa}\n')
            print('TAREFAS: ')
            for t in tarefas:
                print(t)
            input('\nPress enter to exit...')
            
        else:
            print('nada para desfazer.')
            input('\nPress enter to exit...')
            
    elif opcao == 'refazer':
        if desfeitas:
            refazer = desfeitas.pop()
            tarefas.append(refazer)
            print(f'Tarefa refeita: {refazer}\n')
            print('TAREFAS: ')

            for t in tarefas:
                print(t)
            input('\nPress enter to exit...')

        else:
            print('Nada para refazer.')
            input('\nPress enter to exit...')

    elif opcao == 'sair':
        break
    else:
        tarefas.append(opcao)
        print(f'Tarefa adicionada: {opcao}')
        input('\nPress enter to exit...')

print(tarefas)

