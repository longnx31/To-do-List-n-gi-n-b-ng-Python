import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(name, priority="medium"):
    tasks = load_tasks()
    task = {"name": name, "priority": priority, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Đã thêm: {name} (ưu tiên: {priority})")

def list_tasks(filter_priority=None):
    tasks = load_tasks()
    if not tasks:
        print("📭 Không có công việc nào.")
        return

    print("\n📋 Danh sách công việc:")
    for i, task in enumerate(tasks, 1):
        if filter_priority and task["priority"] != filter_priority:
            continue
        status = "✅" if task["done"] else "⏳"
        print(f"{i}. {task['name']} - {status} - Ưu tiên: {task['priority']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index-1]["done"] = True
        save_tasks(tasks)
        print(f"🎯 Đã hoàn thành: {tasks[index-1]['name']}")
    else:
        print("⚠️ Số thứ tự không hợp lệ.")

if __name__ == "__main__":
    print("=== TO-DO LIST (có mức ưu tiên) ===")
    print("1. Thêm công việc")
    print("2. Hiển thị tất cả")
    print("3. Hiển thị theo ưu tiên")
    print("4. Đánh dấu hoàn thành")
    choice = input("Chọn: ")

    if choice == "1":
        name = input("Tên công việc: ")
        priority = input("Ưu tiên (low/medium/high): ").lower()
        add_task(name, priority)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        p = input("Chọn ưu tiên để lọc (low/medium/high): ").lower()
        list_tasks(p)
    elif choice == "4":
        index = int(input("Nhập số thứ tự: "))
        mark_done(index)
    else:
        print("❌ Lựa chọn không hợp lệ.")
