import json

try:
    with open("todo.json", "r") as file:
        task_list = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    task_list = {}

task_tracker = len(task_list)

while True:
    task_tracker += 1
    option = input(">>n: new task, l: display list, e: edit, c: clear todo, tips: for a better usage, j: Developer: ").lower()
    if option == "n":
        task_name = input("the task: ")
        task_sing = {f"task{task_tracker}": {"task_name": task_name, "stat": False}}
        task_list.update(task_sing)
        with open("todo.json", "w") as file:
            json.dump(task_list, file, indent=4)
        print("the task has been added successfully")
    elif option == "l":
        with open("todo.json", "r") as file:
            tasks_display = json.load(file)
        print(json.dumps(tasks_display, indent=4))
    elif option == "e":
        task_edit_pos = input(">>which task you want to edit(example: task1): ")
        if task_edit_pos in task_list:
            edit_type = input(">>n: rename task, d: mark done, x: delete task, c: clear todolist: ")

            if edit_type == "n":
                new_name = input(">>rename: ")
                task_list[task_edit_pos]["task_name"] = new_name
                print(f"{task_edit_pos} has been renamed successfully")
            elif edit_type == "d":
                task_list[task_edit_pos]["stat"] = True
                print(f"{task_edit_pos} has been checked successfully")
            elif edit_type == "x":
                task_list.pop(task_edit_pos)
                print(f"{task_edit_pos} has been deleted successfully")

            with open("todo.json", "w") as file:
                json.dump(task_list, file, indent=4)
    elif option == "c":
        task_list.clear()
        with open("todo.json", "w") as file:
            json.dump(task_list, file)
        print("the todolist has been cleared successfully")
    elif option == "tips":
        print("we prefer that you clear your todo everyday for a cleaner look.")
    elif option == "j":
        print("Developer: JehadCode")

    else:
        break

