

# first create a folder {.vscode } and move launch.json in this folder then run todo_app.py

A simple command-line To-Do List application built with Python.

## Features
- Add tasks with title & category
- View tasks with completion status
- Mark tasks as completed
- Delete tasks
- Persistent storage using JSON file

## How to Run
1. Open terminal in `TODO_APP/`
2. Run commands:

### Add a task
```bash
python todo_app.py add "Finish Assignment" --category Work

#### MArk it Completed 
python todo_app.py complete 1

##### Delete the task 
python todo_app.py delete 1


