import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\n📋 Danh sách công việc:")
    if not tasks:
        print("Chưa có công việc nào!")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Thêm công việc")
        print("2. Xem công việc")
        print("3. Xóa công việc")
        print("4. Thoát")
        choice = input("👉 Chọn chức năng: ")

        if choice == "1":
            task = input("Nhập công việc mới: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Đã thêm công việc.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                idx = int(input("Nhập số thứ tự công việc muốn xóa: ")) - 1
                if 0 <= idx < len(tasks):
                    removed = tasks.pop(idx)
                    save_tasks(tasks)
                    print(f"✅ Đã xóa: {removed}")
                else:
                    print("❌ Số thứ tự không hợp lệ.")
            except ValueError:
                print("❌ Vui lòng nhập số hợp lệ.")
        elif choice == "4":
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
