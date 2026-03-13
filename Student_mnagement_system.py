"""
2. Student Record System  (Swagat,Prasangam,Aayush Dhakal)
Question:
Write a menu driven Python program to manage student records.
===== STUDENT RECORD SYSTEM =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
Description
•	Add Student – Enter student ID, name, and marks.
•	View Students – Display all student records.
•	Search Student – Search student by ID.
•	Update Student – Update marks or name.
•	Delete Student – Remove a student record.

"""


def add():
    print("\n===== Add Student =====")
    s_name = input("Enter Name       : ")
    s_id = input("Enter Student ID : ")
    marks = input("Enter Marks      : ")
    phone_no = input("Enter Phone No   : ")

    with open("student.txt", "a") as f:
        f.write(f"{s_name},{s_id},{marks},{phone_no}\n")

    print("\n✅ Student registered successfully!\n")


def display():
    try:
        with open("student.txt", "r") as f:
            data = f.readlines()

        if not data:
            print("\n⚠ No records found.\n")
            return

        print("\n===== Student Records =====\n")
        print(f"{'Name':<15}{'ID':<10}{'Marks':<10}{'Phone':<15}")
        print("-" * 50)
        for line in data:
            s_name, s_id, marks, phone_no = line.strip().split(",")
            print(f"{s_name:<15}{s_id:<10}{marks:<10}{phone_no:<15}")
        print("-" * 50 + "\n")
    except FileNotFoundError:
        print("\n⚠ File not found.\n")


def update():
    try:
        with open("student.txt", "r") as f:
            data = f.readlines()

        record_id = input("Enter Student ID to update: ")
        found = False

        for i in range(len(data)):
            s_name, s_id, marks, phone = data[i].strip().split(",")
            if s_id == record_id:
                new_name = input("Enter new Name      : ")
                new_marks = input("Enter new Marks     : ")
                new_phone = input("Enter new Phone No  : ")

                data[i] = ",".join([new_name, s_id, new_marks, new_phone]) + "\n"
                found = True
                break

        if found:
            with open("student.txt", "w") as f:
                f.writelines(data)
            print("\n✅ Record updated successfully!\n")
        else:
            print("\n⚠ Student ID not found.\n")

    except FileNotFoundError:
        print("\n⚠ File does not exist.\n")


def search():
    student_id = input("Enter Student ID to search: ")
    try:
        with open("student.txt", "r") as f:
            data = f.readlines()
        if not data:
            print("\n⚠ No records found.\n")
            return

        for line in data:
            s_name, s_id, marks, phone_no = line.strip().split(",")
            if s_id == student_id:
                print("\n===== Student Found =====")
                print(f"Name  : {s_name}")
                print(f"ID    : {s_id}")
                print(f"Marks : {marks}")
                print(f"Phone : {phone_no}\n")
                break
        else:
            print("\n⚠ Student ID not found.\n")
    except FileNotFoundError:
        print("\n⚠ File does not exist.\n")


def delete():
    try:
        with open("student.txt", "r") as f:
            data = f.readlines()
        if not data:
            print("\n⚠ No records found.\n")
            return

        del_id = input("Enter Student ID to delete: ")
        found = False
        with open("student.txt", "w") as f:
            for line in data:
                s_name, s_id, marks, phone_no = line.strip().split(",")
                if s_id == del_id:
                    print("\n===== Record Found =====")
                    print(f"Name  : {s_name}")
                    print(f"ID    : {s_id}")
                    print(f"Marks : {marks}")
                    print(f"Phone : {phone_no}\n")
                    confirm = input("Are you sure you want to delete this record? (yes/no): ").lower()
                    if confirm == "yes":
                        print("\n✅ Record deleted successfully!\n")
                        found = True
                        continue
                f.write(line)
        if not found:
            print("\n⚠ Student ID not found.\n")
    except FileNotFoundError:
        print("\n⚠ File does not exist.\n")


while True:
    print("="*50)
    print("       STUDENT RECORD SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("="*50)
    choice = input("Enter your choice: ")

    if choice == "1":
        add()
    elif choice == "2":
        display()
    elif choice == "3":
        search()
    elif choice == "4":
        update()
    elif choice == "5":
        delete()
    elif choice == "6":
        print("\n👋 See you later!\n")
        break
    else:
        print("\n⚠ Invalid choice! Please try again.\n")
