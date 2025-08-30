import argparse
from utils.file_ops import load_tasks, save_tasks

def add_task(title, category):
    tasks = load_tasks()
    tasks.append({"title": title, "category": category, "completed": False})
    save_tasks(tasks)
    print(f"✅ Task added: {title} ({category})")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\n📋 Your Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✗"
        print(f"{idx}. [{status}] {task['title']} ({task['category']})")

def complete_task(index):
    tasks = load_tasks()
    if 0 <= index-1 < len(tasks):
        tasks[index-1]["completed"] = True
        save_tasks(tasks)
        print(f"🎉 Task marked as completed: {tasks[index-1]['title']}")
    else:
        print("❌ Invalid task number")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index-1 < len(tasks):
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"🗑 Task deleted: {removed['title']}")
    else:
        print("❌ Invalid task number")

def main():
    parser = argparse.ArgumentParser(description="Personal To-Do List App")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("--category", default="General", help="Task category")

    # List tasks
    subparsers.add_parser("list", help="View all tasks")

    # Complete task
    complete_parser = subparsers.add_parser("complete", help="Mark task as completed")
    complete_parser.add_argument("index", type=int, help="Task number to mark complete")

    # Delete task
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("index", type=int, help="Task number to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.category)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.index)
    elif args.command == "delete":
        delete_task(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
