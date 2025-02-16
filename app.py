from datetime import date, datetime, timedelta, timezone
import os

from dotenv import load_dotenv
import streamlit as st
from supabase import create_client, Client
from pydantic import BaseModel


# TODO use SQLAlchemy or Prisma for ORM? and create model for Task
# or check out https://github.com/makridenko/supadantic
# TODO enable RLS in production for tasks table

# Initialize Supabase client
load_dotenv()
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
db: Client = create_client(supabase_url, supabase_key)


class Task(BaseModel):
    id: int
    task: str
    task_date: date
    created_at: datetime


# Function to add a task
def add_task(task: str, task_date: date):
    entry = {
        "task": task,
        "task_date": task_date.isoformat(),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    response = db.table("tasks").insert(entry).execute()
    return response.data


# Function to delete a task
def delete_task(task_id: int):
    db.table("tasks").delete().eq("id", task_id).execute()


# Function to get tasks for a specific date
def get_tasks(task_date: date):
    response = (
        db.table("tasks").select("*").eq("task_date", task_date.isoformat()).execute()
    )
    return response.data


# Function to get all tasks
def get_all_tasks():
    response = db.table("tasks").select("*").order("task_date").execute()
    return response.data


# Streamlit app
st.set_page_config(page_title="Time Audit App", layout="wide")

st.title("Time Audit App")

# Sidebar for input
st.sidebar.header("Log Your Tasks")

# Date selector in sidebar
selected_date = st.sidebar.date_input("Select Date", date.today())

# Create a form for task input
with st.sidebar.form("task_form", clear_on_submit=True):
    # Task input
    task = st.text_input("Enter task")
    submitted = st.form_submit_button("Add Task", use_container_width=True)
    
    if submitted:
        if task:
            add_task(task, selected_date)
            st.success("Task added successfully!")
        else:
            st.error("Please enter a task.")

# Main content area
st.header(f"Tasks for {selected_date}")

# Add tab selection for different views
tab1, tab2 = st.tabs(["Daily View", "All Tasks"])

with tab1:
    # Date selector for viewing tasks
    view_date = st.date_input("Select Date to View", date.today())

    # Display tasks
    tasks = get_tasks(view_date)
    for task in tasks:
        col1, col2 = st.columns([5, 1])
        with col1:
            st.write(task["task"])
        with col2:
            if st.button("X", key=task["id"]):
                delete_task(task["id"])
                st.rerun()

with tab2:
    st.header("All Tasks")
    all_tasks = get_all_tasks()
    
    # Group tasks by date
    current_date = None
    for task in all_tasks:
        task_date = datetime.fromisoformat(task["task_date"]).date()
        
        # Show date header when date changes
        if current_date != task_date:
            st.subheader(task_date.strftime("%B %d, %Y"))
            current_date = task_date
        
        # Display task with delete button
        col1, col2 = st.columns([5, 1])
        with col1:
            st.write(task["task"])
        with col2:
            if st.button("X", key=f"all_{task['id']}"):
                delete_task(task["id"])
                st.rerun()
