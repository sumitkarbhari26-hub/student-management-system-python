
students = []

def add_student():
    name = input("Enter student name: ")
    usn = input("Enter student USN: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "usn": usn,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    for student in students:
        print("\n--- Student Details ---")
        print("Name:", student["name"])
        print("USN:", student["usn"])
        print("Marks:", student["marks"])

while True:
    print("\n--- STUDENT MANAGEMENT SYSTEM ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
