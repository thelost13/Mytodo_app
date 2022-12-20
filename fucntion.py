filepath_global = "todo.txt"


def get_todos(filepath = filepath_global):
    """ Read a text file and return the list  of to do items    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = filepath_global) :
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main14__":
    print("hello from the other side")
    print(get_todos())