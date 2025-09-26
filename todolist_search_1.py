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

def search_tasks(tasks):
    keyword = input("Nhập từ khoá để tìm: ").lower()
    found = [task for task in tasks if keyword in task["title"].lower()]
    if found:
        print("\n🔍 Kết quả tìm kiếm:")
        for i, task in enumerate(found, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} {status}")
    else:
        print("⚠️ Không tìm thấy công việc nào khớp.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== ToDoList Menu ===")
        print("1. Xem danh sách")
        print("2. Thêm công việc")
        print("3. Tìm kiếm công việc")
        print("4. Thoát")

        choice = input("Chọn: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            search_tasks(tasks)
        elif choice == "4":
            print("👋 Thoát chương trình.")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
