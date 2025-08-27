import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("📭 Không có việc nào trong danh sách.")
    else:
        print("\n📋 Danh sách công việc:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} {status}")

def add_task(tasks):
    title = input("Nhập tên công việc: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("➕ Đã thêm công việc!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Chọn số công việc đã xong: ")) - 1
        tasks[idx]["done"] = True
        save_tasks(tasks)
        print("✔️ Đã cập nhật trạng thái!")
    except (ValueError, IndexError):
        print("⚠️ Lựa chọn không hợp lệ.")

def main():
    tasks = load_tasks()
    while True:
        print("\n===
