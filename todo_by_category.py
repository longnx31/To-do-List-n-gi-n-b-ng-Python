import os

FILENAME = "tasks_by_category.txt"

def load_tasks():
    tasks = {"Work": [], "Personal": [], "Study": []}
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                category, task = line.strip().split("|", 1)
                if category in tasks:
                    tasks[category].append(task)
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as file:
        for category, task_list in tasks.items():
            for task in task_list:
                file.write(f"{category}|{task}\n")

def show_tasks(tasks):
    print("\n📋 Danh sách công việc theo nhóm:")
    for category, task_list in tasks.items():
        print(f"\n📂 {category}:")
        if not task_list:
            print("  (Trống)")
        else:
            for idx, task in enumerate(task_list, 1):
                print(f"  {idx}. {task}")

def choose_category():
    print("\nChọn nhóm công việc:")
    print("1. Work")
    print("2. Personal")
    print("3. Study")
    cat_choice = input("👉 Chọn số: ").strip()
    return {"1": "Work", "2": "Personal", "3": "Study"}.get(cat_choice, None)

def main():
    tasks = load_tasks()

    while True:
        print("\n📌 Menu To-Do")
        print("1. Thêm công việc")
        print("2. Xem công việc")
        print("3. Xóa công việc")
        print("4. Thoát")
        choice = input("👉 Chọn thao tác: ").strip()

        if choice == "1":
            category = choose_category()
            if not category:
                print("❌ Nhóm không hợp lệ.")
                continue
            task = input("Nhập công việc mới: ")
            tasks[category].append(task)
            save_tasks(tasks)
            print("✅ Đã thêm công việc.")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            category = choose_category()
            if not category:
                print("❌ Nhóm không hợp lệ.")
                continue
            if not tasks[category]:
                print("📂 Nhóm này chưa có công việc.")
                continue
            show_tasks({category: tasks[category]})
            try:
                idx = int(input("Nhập số thứ tự công việc cần xóa: ")) - 1
                if 0 <= idx < len(tasks[category]):
                    removed = tasks[category].pop(idx)
                    save_tasks(tasks)
                    print(f"🗑️ Đã xóa: {removed}")
                else:
                    print("❌ Số không hợp lệ.")
            except ValueError:
                print("❌ Vui lòng nhập số.")

        elif choice == "4":
            print("👋 Hẹn gặp lại!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
