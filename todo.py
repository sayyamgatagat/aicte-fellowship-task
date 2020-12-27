import sys
import os
import datetime


def add_todo(task):
    addfile = open("todo.txt", 'a')
    addfile.write(task + '\n')
    print("Added todo: " + f'"{task}"')
    addfile.close()


def display():
    try:
        if os.stat("todo.txt").st_size > 0:
            file = open("todo.txt", "r")
            tasks = file.readlines()
            n = len(tasks)
            if n > 0:
                task_text = ""
                for i in range(n, 0, -1):
                    task_text += f'{[i]} ' + tasks[i - 1]
                print(sys.stdout.buffer.write(task_text.encode('utf8')))
                file.close()
        else:
            print("There are no pending todos!")
    except OSError:
        print("There are no pending todos!")


def mark_done(task_number):
    file = open("todo.txt", "r")
    done_file = open("done.txt", "a")
    tasks = file.readlines()
    file.close()
    if 0 < int(task_number) <= len(tasks):
        file = open("todo.txt", "w")
        removed_task = tasks.pop(int(task_number) - 1)
        print(f"Marked todo #{task_number} as done.")
        done_file.write(removed_task)
        file.writelines(tasks)
        file.close()
        done_file.close()
    else:
        print(f"Error: todo #{task_number} does not exist.")


def delete_todo(task_number):
    file = open("todo.txt", "r")
    tasks = file.readlines()
    file.close()
    if 0 < int(task_number) <= len(tasks):
        print(f"Deleted todo #{task_number}")
        file = open("todo.txt", "w")
        tasks.pop(int(task_number) - 1)
        file.writelines(tasks)
        file.close()
    else:
        print(f"Error: todo #{task_number} does not exist. Nothing deleted.")


def report():
    completed = open("done.txt", "r")
    pending = open("todo.txt", "r")
    pending_tasks = pending.readlines()
    completed_tasks = completed.readlines()
    print(
        f"{datetime.datetime.today().strftime('%Y-%m-%d')} Pending : {len(pending_tasks)} Completed : {len(completed_tasks)}")


n = len(sys.argv) - 1
sys.argv.pop(0)

help_text = '''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''

if n == 0 or sys.argv[0] == 'help':
    print(sys.stdout.buffer.write(help_text.encode('utf8')))

if n > 0:
    if sys.argv[0] == 'add':
        if n == 1:
            print("Error: Missing todo string. Nothing added!")
        else:
            add_todo(sys.argv[1])
    if sys.argv[0] == 'ls':
        display()
    if sys.argv[0] == 'del':
        if n == 1:
            print("Error: Missing NUMBER for deleting todo.")
        else:
            delete_todo(sys.argv[1])
    if sys.argv[0] == 'done':
        if n == 1:
            print("Error: Missing NUMBER for marking todo as done.")
        else:
            mark_done(sys.argv[1])
    if sys.argv[0] == 'report':
        report()
