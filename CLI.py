from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        # using with as we don't have to manually close the file

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos("todos.txt")

        # new_todos = []
        #
        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number -= 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            completed_todo = int(user_action[9:])

            todos = get_todos()
            todo_to_remove = todos[completed_todo - 1].strip('\n')
            todos.pop(completed_todo - 1)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the todo list"
            print(message)
        except IndexError:
            print("There is no such todo in the todo list")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is invalid.")
print("Bye!")
