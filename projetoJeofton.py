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

