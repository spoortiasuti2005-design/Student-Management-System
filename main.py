import json

FILE_NAME = "students.json"


# Load student records
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# Save student records
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add a student
def add_student():
    students = load_students()

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty!")
        return

    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists!")
            return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

    age = input("Enter Student Age: ").strip()

    if not age.isdigit() or int(age) <= 0:
        print("Please enter a valid positive age!")
        return

    course = input("Enter Student Course: ").strip()

    if not course:
        print("Course cannot be empty!")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


# View all students
def view_students():
    students = load_students()

    if not students:
        print("No student records found.")
        return

    print("\n" + "=" * 65)
    print("{:<12} {:<15} {:<10} {:<15}".format(
        "Student ID", "Name", "Age", "Course"
    ))
    print("=" * 65)

    for student in students:
        print("{:<12} {:<15} {:<10} {:<15}".format(
            student["id"],
            student["name"],
            student["age"],
            student["course"]
        ))

    print("=" * 65)


# Search for a student
def search_student():
    students = load_students()

    student_id = input("Enter Student ID to search: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found!")
            print("=" * 65)
            print("{:<12} {:<15} {:<10} {:<15}".format(
                "Student ID", "Name", "Age", "Course"
            ))
            print("=" * 65)

            print("{:<12} {:<15} {:<10} {:<15}".format(
                student["id"],
                student["name"],
                student["age"],
                student["course"]
            ))

            print("=" * 65)
            return

    print("Student not found.")
# Update student details
def update_student():
    students = load_students()
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            print("Student Found:", student)

            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["course"] = input("Enter new course: ")

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete a student
# Delete a student
def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ").strip()

    for student in students:
        if student["id"] == student_id:
            print("Student Found:", student)

            confirm = input("Are you sure you want to delete? (yes/no): ").lower()

            if confirm == "yes":
                students.remove(student)
                save_students(students)
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled!")

            return

    print("Student not found.")

# Main menu
def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()