
"""
To Do List app - Web App Version
"""

import streamlit as st
import funcs

todolist = funcs.get_todo_list()


def add_todo():
    new_todo = st.session_state["todo_txb"]
    print(new_todo)
    todolist.append(new_todo + "\n")
    funcs.post_todo_list(todolist)


def complete_todo():
    print("hi")


st.title("My Todo List App")
st.subheader("Welcome to the 'My Todo List' App!")
st.write("This app was made with the hopes of increasing productivity.")
st.write("Good Luck! - Antonio M")


for index, todo in enumerate(todolist):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todolist.pop(index)
        funcs.post_todo_list(todolist)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a todo",
              placeholder="...",
              on_change=add_todo,
              key='todo_txb')
