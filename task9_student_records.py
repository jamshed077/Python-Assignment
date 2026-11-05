# Task 9: Student Record Management System
students = {}   # roll_no -> {"name":..., "branch":..., "marks":...}

def add_student():
    roll = input("Enter Roll No: ").strip()
    if roll in students:
        print("Roll number already exists!")
        return
    name = input("Enter Name: ").strip()
    branch = input("Enter Branch: ").strip()
    marks = float(input("Enter Marks: "))
    students[roll] = {"name": name, "branch": branch, "marks": marks}
    print("Student added successfully!")

def display_all():
    if not students:
        print("No records found.")
        return
    print(f"\n{'Roll No':<10}{'Name':<20}{'Branch':<10}{'Marks':<8}")
    print("-" * 48)
    for roll, d in students.items():
        print(f"{roll:<10}{d['name']:<20}{d['branch']:<10}{d['marks']:<8}")

def search_student():
    key = input("Enter name to search: ").strip().lower()
    found = False
    for roll, d in students.items():
        if key in d["name"].lower():
            print(f"Found -> Roll: {roll}, Name: {d['name']}, "
                  f"Branch: {d['branch']}, Marks: {d['marks']}")
            found = True
    if not found:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll No to delete: ").strip()
    if roll in students:
        del students[roll]
        print("Record deleted.")
    else:
        print("Roll number not found.")

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        display_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank you! Goodbye.")
        break
    else:
        print("Invalid choice, try again.")
