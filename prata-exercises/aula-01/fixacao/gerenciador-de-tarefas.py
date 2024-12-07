# Gerenciamento de Tarefas
# Crie uma lista chamada tarefas que contenha cinco tarefas diferentes que você precisa realizar.
# Peça ao usuário para adicionar uma nova tarefa à lista e imprima a lista atualizada.
# Peça ao usuário para informar o índice de uma tarefa que deseja remover da lista e imprima a lista atualizada.
# Imprima todas as tarefas no conforme o exemplo abaixo:
# [ ] lavar louça
# [ ] comprar carne
# [ ] estudar programação

# Peça ao usuário para marcar uma tarefa como concluída. Ele irá informar o índice de uma tarefa que foi concluída e a remover da lista de tarefas pendentes.
# Conte quantas tarefas ainda estão pendentes e mostre na tela.
# Faça um menu com as opções de adicionar, remover, mostrar tarefas pendentes, marcar como concluída e contar quantas tarefas estão pendentes.


def task_list():
    """"Listando Tarefas
    """
    for i in range(len(tasks)):
        print(f"[{i}] - {tasks[i]}")

def add_task(new_task:str,tasks:list):
    """
    Adicionando tarefas
    """
    tasks.append(new_task)

def remove_task(index:int, tasks:list):
    """Removendo tarefas

    Args:
        index (int): recebe um número inteiro referente a posição da tarefa desejada
        tasks (list): lista de tarefas que deseja alterar.

    Returns:
        lista de tarefas atualizadas.
    """
    tasks.pop(index)
    return f'Tarefa{tasks[index]} removida com sucesso;'

def count_tasks(tasks:list):
    """Contando tarefas

    Args:
        tasks (list): lista de tarefas desejada

    Returns:
        Quantidade de tarefas existente na lista
    """
    pendind_tasks = len(tasks)

    return pendind_tasks

    




tasks = ['Estudar','Trabalhar','Correr','Preparar Aula']


print("*"*10,"|",'TASK MANAGER',"|","*"*48,"")
print("*"*20,"|",'SEJA BEM VINDO AO GERENCIADOR DE TAREFAS',"|","*"*10,"")
print("*"*30,"|",'DO',"|","*"*38,"")
print("*"*40,"|",'DOUGLINHAS',"|","*"*20,"")


new_task = input('Digite o nome de uma nova tarefa para adicionar a lista de tarefas: ')
new_task = new_task.capitalize()
add_task(new_task,tasks)
task_list()
del_task = int(input('Digite o número de uma tarefa que deseja marcar como concluída'))
remove_task(del_task,tasks)
print(tasks)




#print(new_task)
# task_list()

