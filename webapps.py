import streamlit as sk
import fucntion

todos = fucntion.get_todos()

def add_todo():
    todo = sk.session_state['new_todo'] + "\n"
    todos.append(todo)
    fucntion.write_todos(todos)

sk.title("Todo App")
sk.subheader("This my todo App")
sk.write("This app is to increase my productivity")

for index, todo in enumerate(todos):
    checkbox = sk.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fucntion.write_todos(todos)
        del sk.session_state[todo]
        sk.experimental_rerun()

sk.text_input(label="", placeholder="Enter a task",on_change=add_todo, key='new_todo')