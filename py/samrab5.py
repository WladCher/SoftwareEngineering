import os

def add_task():
    task = input("Введите новую задачу: ")
    with open("tasks.txt", "a", encoding="utf-8") as file:
        file.write(task + "\n")

def show_tasks():
    if not os.path.exists("tasks.txt"):
        print("Список задач пока пуст.")
        return
    with open("tasks.txt", encoding="utf-8") as file:
        tasks = [line.strip() for line in file if line.strip()]
    print("\nВаши задачи:")
    for num, task in enumerate(tasks, 1):
        print(f"{num}. {task}")

if __name__ == "__main__":
    add_task()
    show_tasks()