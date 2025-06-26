tasks = []
print("\n......Welcome to the TO-Do List App.......")
def schedule_task():
    user_input = input("Enter one or more tasks (separated by commas): 📑  ").strip()
    
    if not user_input:
        print("❗ No task entered.")
        return

    task_list = [task.strip() for task in user_input.split(',') if task.strip()]

    if not task_list:
        print("❗No valid tasks found.")
        return

    for task_name in task_list:
        tasks.append({"name": task_name, "completed": False})

    print(f"\n✅ Scheduled {len(task_list)} task(s):")
    for index, task_name in enumerate(task_list, start=1):
        print(f"{index}. {task_name}")

    

def view_task():
    if not tasks:
        print("No Task added,The List is Empty")
        return
    
    print("Your TO-Do List:")
    for index, task in enumerate(tasks,start = 1):
        name = task['name']
        if task['completed']:
            name += "(Completed)"
        print(f"{index}.{name}")

def mark_task_completed():
    if not tasks:
        print("📭 No tasks to update.")
        return

    view_task()

    try:
        task_index = int(input(f"Enter the task number to mark as completed (1 to {len(tasks)}): ")) - 1
        if 0 <= task_index < len(tasks):
            if tasks[task_index]["completed"]:
                print("✅ Task is already marked as completed.")
            else:
                tasks[task_index]["completed"] = True
                print(f"✅ Task '{tasks[task_index]['name']}' marked as completed!")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")
   

def delete_task():
    if not tasks:
        print("No tasks to delete.👎")
        return
    
    view_task()
    try:
        task_index =int(input("Enter the task number to delete:")) -1
        task_name = tasks[task_index]['name']
        if 0 <= task_index < len(tasks):
            confirm = input(f"Delete task '{task_name}'?(yes/no):").strip().lower()
            if confirm == 'yes':
                del tasks[task_index]
                print("Task Deleted!")
            else:
                print("Deletion Cancelled.❌")
        else:
            print("Invalid Task Number. ⁉️")
    except ValueError:
            print("Please enter a valid number.")

while True:
    print("\n ")
    print("1️⃣  ➕  Schedule Tasks")
    print("2️⃣  👀  View Task")
    print("3️⃣  ✔️  Mark task as Completed")
    print("4️⃣  🗑️  Delete Task")
    print("5️⃣  🚪 Exit")
    choice = input("Enter your choice 1️⃣  - 4️⃣ : ")
    
    if choice == "1":
        schedule_task()
    
    elif choice == "2":
        view_task()

    elif choice == "3":
        mark_task_completed()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("✅ Thank you for Using The App. Stay organized and have a  Productive day. 📑")
        break
    else:
        print("Invalid choice.Please enter a number from 1 to 4")
