# Student Management System

A simple console-based Student Management System developed using Python. It allows users to manage student records through a menu-driven interface.

## Features

- Add new student records.
- View all student records in a formatted table.
- Search for a student using Student ID.
- Update existing student details.
- Delete student records with confirmation.
- Validate student inputs.
- Prevent duplicate Student IDs.
- Store student data permanently using a JSON file.

## Technologies Used

- Python 3
- JSON

## Project Structure

```text
Student-Management-System/
│
├── main.py
├── students.json
└── README.md
```

## Code Explanation

The project is divided into different functions to make the program simple and easy to understand.

### 1. Import JSON Module

```python
import json

FILE_NAME = "students.json"
```

- `import json` imports Python's JSON module.
- `FILE_NAME` stores the name of the file used to save student records.

### 2. Load Student Records

**Function:** `load_students()`

- Reads existing student records from the JSON file.
- Uses `json.load()` to retrieve data.
- Returns an empty list if the file does not exist.

### 3. Save Student Records

**Function:** `save_students(students)`

- Saves student records into `students.json`.
- Uses `json.dump()` to convert Python data into JSON format.
- Uses `indent=4` to make the file readable.

### 4. Add a Student

**Function:** `add_student()`

- Takes Student ID, name, age and course as input.
- Checks for empty values and duplicate Student IDs.
- Validates the student's age.
- Stores student details in a dictionary.
- Adds the student to the list and saves the records.

### 5. View All Students

**Function:** `view_students()`

- Displays all stored student records.
- Uses a `for` loop to access each student.
- Displays the information in a formatted table.
- Shows a message if no records are available.

### 6. Search for a Student

**Function:** `search_student()`

- Takes Student ID as input.
- Searches for the matching student using a `for` loop.
- Displays the student's details if found.
- Displays a message if the student does not exist.

### 7. Update Student Details

**Function:** `update_student()`

- Searches for a student using Student ID.
- Displays the current student details.
- Takes new name, age and course as input.
- Validates the new information.
- Updates the student record and saves the changes.

### 8. Delete a Student

**Function:** `delete_student()`

- Searches for a student using Student ID.
- Asks the user for confirmation before deletion.
- Deletes the record if the user enters `yes`.
- Cancels deletion if the user enters `no`.
- Saves the updated student records.

### 9. Main Menu

**Function:** `main()`

- Displays the menu with six options.
- Uses a `while` loop to keep the program running.
- Uses `if` and `elif` conditions to process user choices.
- Calls the appropriate function based on the selected option.
- Uses `break` to exit the program.

### 10. Program Starting Point

```python
if __name__ == "__main__":
    main()
```

This statement calls the `main()` function when the Python file is executed directly.

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

## Concepts Learned

- Python functions
- Conditional statements
- Loops
- Lists and dictionaries
- File handling
- JSON data storage
- Input validation
- CRUD operations (Create, Read, Update, Delete)

## Author

**Spoorti Asuti**

GitHub: [Spoorti Asuti](https://github.com/spoortiasuti2005-design)