import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Tải danh sách công việc từ file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks(tasks):
    """Lưu danh sách công việc vào file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Hiển thị danh sách công việc."""
    if not tasks:
        print("📌 Danh sách công việc trống!")
    else:
        print("\n📋 Danh sách công việc:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("-" * 30)

def main():
    tasks = load_tasks()

    while True:
        print("\n🎯 To-Do List")
        print("1️⃣ Thêm công việc")
        print("2️⃣ Xóa công việc")
        print("3️⃣ Hiển thị danh sách")
        print("4️⃣ Thoát")

        choice = input("Chọn thao tác (1-4): ").strip()

        if choice == "1":
            task = input("Nhập công việc mới: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("✅ Đã thêm công việc!")

        elif choice == "2":
            display_tasks(tasks)
            try:
                index = int(input("Nhập số thứ tự công việc cần xóa: ")) - 1
                if 0 <= index < len(tasks):
                    removed_task = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"🗑️ Đã xóa: {removed_task}")
                else:
                    print("⚠️ Số thứ tự không hợp lệ!")
            except ValueError:
                print("⚠️ Vui lòng nhập số hợp lệ!")

        elif choice == "3":
            display_tasks(tasks)

        elif choice == "4":
            print("👋 Thoát chương trình. Hẹn gặp lại!")
            break

        else:
            print("⚠️ Lựa chọn không hợp lệ! Vui lòng nhập 1-4.")

if __name__ == "__main__":
    main()
