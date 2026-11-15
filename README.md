# Student Management System

## 1. Project Description

The Student Management System is a beginner-friendly Python project used to manage student records. It allows users to add, view, search, update, and delete student information.

The program stores student details in a JSON file, so the records remain saved even after the program is closed.

## 2. Features

- **Add Student:** Add a new student with ID, name, age, and course.
- **View Students:** Display all stored student records.
- **Search Student:** Find a student using their unique ID.
- **Update Student:** Modify an existing student's details.
- **Delete Student:** Remove a student record using their ID.
- **Exit:** Close the application.

## 3. Technologies Used

- **Python:** Used to develop the application and implement its functionality.
- **JSON:** Used to store and retrieve student records.
- **VS Code:** Used to write and run the Python program.

## 4. Explanation of the Program

### A. Importing the JSON Module

The `json` module is imported to read and write student information in JSON format.

### B. File Name

The variable `FILE_NAME` stores the name of the file (`students.json`) where student records are saved.

### C. Loading Student Records

The `load_students()` function:
- Opens the `students.json` file.
- Reads the stored student records.
- Returns an empty list if the file does not exist.

### D. Saving Student Records

The `save_students()` function:
- Opens the JSON file in write mode.
- Saves the student records.
- Uses indentation to make the JSON data readable.

### E. Adding a Student

The `add_student()` function:
- Takes student ID, name, age, and course as input.
- Checks whether the student ID already exists.
- Adds the new student to the list.
- Saves the updated records in the JSON file.

### F. Viewing Students

The `view_students()` function:
- Loads all student records.
- Displays the records.
- Shows a message if no student records are available.

### G. Searching for a Student

The `search_student()` function:
- Asks the user to enter a student ID.
- Searches for the matching ID.
- Displays the student's details if found.

### H. Updating Student Details

The `update_student()` function:
- Searches for a student using their ID.
- Allows the user to enter new details.
- Saves the updated information.

### I. Deleting a Student

The `delete_student()` function:
- Searches for a student using their ID.
- Removes the matching record.
- Saves the updated list in the JSON file.

### J. Main Function

The `main()` function displays a menu with six options. It uses a `while` loop and `if-elif-else` statements to perform the selected operation until the user chooses Exit.

## 5. Project Folder Structure

```text
Student-Management-System/
│
├── main.py
├── students.json
└── README.md
```

- `main.py` – Contains the Python program.
- `students.json` – Stores student records.
- `README.md` – Contains project information and explanations.

## 6. How to Run the Project

1. Download or clone the repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the command:

```bash
python main.py
```

5. Select an option from the menu and follow the instructions.

## 7. Concepts Learned

- Python functions
- Lists and dictionaries
- Loops and conditional statements
- User input and output
- File handling
- JSON data storage
- Basic CRUD operations (Create, Read, Update, Delete)

## 8. Developed By

**Spoorti Asuti**

Computer Science and Engineering Student


## 9. Sample Program Output

When the program runs, the following menu is displayed:

```text
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Enter your choice:
```

### Example: Adding a Student

```text
Enter your choice: 1
Enter Student ID: 101
Enter Student Name: Spoorti
Enter Student Age: 21
Enter Student Course: CSE

Student added successfully!
```

### Example: Viewing Students

```text
Enter your choice: 2

{'id': '101', 'name': 'Spoorti', 'age': '21', 'course': 'CSE'}
```

*Note: This is an illustrative example. Your actual output may differ depending on the records entered.*