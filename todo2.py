import json
import os

FILE_NAME = "tasks.json"

# Load danh sách công việc từ file JSON (nếu có)
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Lưu danh sách công việc vào file JSON
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Hiển thị danh sách công việc
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Danh sách công việc trống.")
    else:
        print("\n📌 Danh sách công việc:")
        for i, task in enumerate(tasks, 1):
            status = "✅ Hoàn thành" if task["done"] else "❌ Chưa xong"
            print(f"{i}. {task['task']} - {status}")

# Thêm công việc mới
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"✅ Đã thêm công việc: {task}")

# Xóa công việc theo số thứ tự
def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Đã xóa: {removed_task['
