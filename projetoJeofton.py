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
