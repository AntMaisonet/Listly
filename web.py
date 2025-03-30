
"""
Listly - A to-do list app - Web App Version
"""

import streamlit as st
import funcs

todolist = funcs.get_todo_list()


def add_todo():
    new_todo = st.session_state["todo_txb"]
    new_todo = new_todo + "\n"

    if new_todo in todolist:
        st.error("⚠️ Duplicate Item - This item already exists in the list ⚠️")
    else:
        todolist.append(new_todo)
        funcs.post_todo_list(todolist)

st.write("Coded with Python and Love by Antonio Maisonet")
st.title("Listly - Your Tasks, Simplified.")
st.subheader("A lightweight and minimalistic to-do list app that helps you stay productive without distractions")

for index, todo in enumerate(todolist):
    checkbox = st.checkbox(f"{index}. {todo}", key=todo)
    if checkbox:
        todolist.pop(index)
        funcs.post_todo_list(todolist)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo",
              placeholder="...",
              on_change=add_todo,
              key='todo_txb')