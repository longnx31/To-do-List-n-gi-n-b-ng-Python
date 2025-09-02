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

def edit_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Chọn số công việc muốn sửa: ")) - 1
        if 0 <= idx < len(tasks):
            new_title = input("Nhập tên mới: ")
            tasks[idx]["title"] = new_title
            save_tasks(tasks)
            print("✏️ Đã cập nhật công việc!")
        else:
            print("⚠️ Lựa chọn không hợp lệ.")
    except ValueError:
        print("⚠️ Nhập sai định dạng.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== ToDoList Menu ===")
        print("1. Xem danh sách")
        print("2. Thêm công việc")
        print("3. Sửa tên công việc")
        print("4. Thoát")

        choice = input("Chọn: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            print("👋 Thoát chương trình.")
            break
        else:
            print("⚠️ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
