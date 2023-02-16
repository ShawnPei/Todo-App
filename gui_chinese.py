import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkGrey6")
clock = sg.Text('', key="clock")
label = sg.Text("输入待办事项")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("添加")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("修改")
complete_button = sg.Button("完成")
exit_button = sg.Button("退出")
# layout expects a list, the element will be put in a row if put in one list
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%Y/%m/%d， %H:%M:%S"))

    match event:
        case "添加":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "修改":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select items first.", font=('Helvetica', 20))

        case "完成":
            try:
                todo_to_delete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_delete)
                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select items first.", font=('Helvetica', 20))

        case "退出":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break



window.close()

