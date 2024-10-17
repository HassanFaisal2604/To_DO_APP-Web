import streamlit as st
import functions 
todos=functions.read_tasks()

st.title("Welcome to the To-Do App!")
st.subheader("Add tasks") 
def add_todo():
    todo=st.session_state["new_todo"]
    functions.add_task(todo)
    st.experimental_fragment()

for index,todo in enumerate(todos):
    box=st.checkbox(todo,key=todo)
    if box:
        functions.delete_task(todo)
        del st.session_state[todo]
        st.experimental_fragment()
        
input_user=st.text_input(label="",placeholder="add new todo",on_change=add_todo,key='new_todo')
st.subheader("Previous task")
old_todos=functions.read_completed_tasks()
for index,values in enumerate (old_todos):
    st.write(values) 
