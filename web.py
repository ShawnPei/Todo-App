import os

import streamlit as st
import functions

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)

# def complete_todo():

# The order of the code is important
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
