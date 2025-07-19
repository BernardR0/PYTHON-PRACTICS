from tarefa import Tarefa

lista_de_tarefas = []

def criar_tarefa(titulo, descricao):
    task = Tarefa(titulo, descricao)
    lista_de_tarefas.append(task)        

def remover_tarefa(id_tarefa):
    for tarefa in lista_de_tarefas:
        if tarefa.id == id_tarefa:
            lista_de_tarefas.remove(tarefa)
            print(f"Tarefa '{tarefa}' removida com sucesso.")
            return
    print(f"Nenhuma tarefa com ID {id_tarefa} foi encontrada.")

def mostrar_tarefas():
    if not lista_de_tarefas:
        print("Nenhuma tarefa encontrada.\n")
    else:
        for tarefa in lista_de_tarefas:
            print(tarefa)

def concluir_tarefa(value):
    for tarefa in lista_de_tarefas:
        if tarefa.id == value:
            confirmacao = str(input('Deseja concluir essa tarefa?(y/n) '))           
            tarefa.definir_conclusao(confirmacao)

sair = False

while not sair:

    from tarefa import Tarefa

    print("1 - Adicionar Tarefa")
    print("2 - Remover Tarefa")
    print("3 - Mostrar Tarefas")
    print("4 - Concluir Tarefas")
    print("5 - Sair\n")

    opcao = input("Selecione uma opcao no menu: ")

    if opcao == '1':
        titulo = input("Escreva um titulo: ")
        descricao = input("Adicione uma descricao: ")
        criar_tarefa(titulo, descricao)

    elif opcao == '2':
        try:
            id_tarefa = int(input("Digite o id da tarefa a ser removida: "))
            remover_tarefa(id_tarefa)
        except ValueError:
            print("Por favor, digite um número válido para o ID.")

    elif opcao == '3':
        mostrar_tarefas()

    elif opcao == '4':
       id = int(input("Qual o ID da tarefa que deseja concluir?"))
       concluir_tarefa(id)
        
    elif opcao == '5':
        sair = True

    else:
        print("Opção inválida. Tente novamente.")
