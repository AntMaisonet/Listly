FILEPATH = "TodoList.txt"


def get_todo_list(filepath=FILEPATH):
    """ Reads a txt file and returns a list
    of to do items."""
    with open(filepath, 'r') as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def post_todo_list(todo_list_arg, filepath=FILEPATH):
    """ Writes the to do items from
    a list to a txt file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_list_arg)
    return None


if __name__ == "__main__":
    print("Hello from funcs.py!")



