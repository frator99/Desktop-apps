FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    #legge il file che contiene la to-do list
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    #aggiunge un'azione nella to-do list
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#qui controlliamo se lo script è stato eseguito direttamente da questo file o se è stato richiamato
# da un frontend:
if __name__ == "__main__":
    print("hello")
    print(get_todos())

