tarefas = []  

def adicionar_tarefa(descricao):
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa na lista.")
        return
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['descricao']} - {status}")
def marcar_concluida(indice):
    if 1 <= indice <= len(tarefas):
        tarefas[indice-1]["concluida"] = True
        print(f"Tarefa '{tarefas[indice-1]['descricao']}' marcada como concluída!")
    else:
        print("Índice inválido!")

def remover_tarefa(indice):
    if 1 <= indice <= len(tarefas):
        tarefa_removida = tarefas.pop(indice-1)
        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")
    else:
        print("Índice inválido!")

def menu():
    while True:
        print("\n=== Lista de Tarefas ===")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        if opcao == "1":
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao)
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a marcar como concluída: "))
                marcar_concluida(indice)
            except ValueError:
                print("Por favor, digite um número válido!")
        elif opcao == "4":
            listar_tarefas()
            try:
                indice = int(input("Digite o número da tarefa a remover: "))
                remover_tarefa(indice)
            except ValueError:
                print("Por favor, digite um número válido!")
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()