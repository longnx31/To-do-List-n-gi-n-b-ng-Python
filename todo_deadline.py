import json
import os
from datetime import datetime, timedelta

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(name, deadline_str):
    try:
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
    except ValueError:
        print("⚠️ Ngày không hợp lệ! Vui lòng nhập theo định dạng YYYY-MM-DD.")
        return

    tasks = load_tasks()
    tasks.append({
        "name": name,
        "deadline": deadline_str,
        "done": False
    })
    save_tasks(tasks)
    print(f"✅ Đã thêm: {name} (hết hạn: {deadline_str})")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 Không có công việc nào.")
        return

    print("\n📋 Danh sách công việc:")
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "⏳"
        print(f"{i}. {t['name']} - {status} - Hạn: {t['deadline']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"🎯 Đã hoàn thành: {tasks[index - 1]['name']}")
    else:
        print("⚠️ Số thứ tự không hợp lệ.")

def list_urgent():
    tasks = load_tasks()
    today = datetime.now().date()
    upcoming = [t for t in tasks if not t["done"] and
                datetime.strptime(t["deadline"], "%Y-%m-%d").date() <= today + timedelta(days=3)]
    
    if not upcoming:
        print("🎉 Không có công việc nào sắp hết hạn.")
        return

    print("\n🔥 Công việc sắp hết hạn (3 ngày tới):")
    for t in upcoming:
        print(f"⚠️ {t['name']} - Hạn: {t['deadline']}")

if __name__ == "__main__":
    print("=== TO-DO LIST (với Deadline) ===")
    print("1. Thêm công việc")
    print("2. Hiển thị danh sách")
    print("3. Đánh dấu hoàn thành")
    print("4. Xem công việc sắp hết hạn")
    choice = input("Chọn: ")

    if choice == "1":
        name = input("Tên công việc: ")
        deadline = input("Deadline (YYYY-MM-DD): ")
        add_task(name, deadline)
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        index = int(input("Nhập số thứ tự: "))
        mark_done(index)
    elif choice == "4":
        list_urgent()
    else:
        print("❌ Lựa chọn không hợp lệ.")
