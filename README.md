# 🎓 Student Management System (CLI)

A simple, robust command-line application written in Python for managing student records. 
It allows users to perform CRUD operations, manage grades, calculate averages, and generate class statistics, with all data persisted in a JSON file.

## ✨ Features

*   **Add Students**: Create new student profiles with unique IDs and name validation.
*   **View Students**: Display all stored student records.
*   **Search & Delete**: Find specific students by ID or remove them from the system.
*   **Grade Management**: Add grades (0-20 scale) and view individual student transcripts.
*   **Statistics Engine**: 
    *   Calculate individual student averages.
    *   Determine class-wide average.
    *   Identify the highest and lowest performing students (handling ties).
    *   Assign qualitative appreciation (e.g., "Good", "Excellent").
*   **Data Persistence**: Automatically saves data to `etudiants.json` and loads it on startup.
*   **Robust Error Handling**: Validates user input (numeric values, ID uniqueness, grade ranges) and handles corrupted/missing JSON files gracefully.

## 🛠️ Technologies Used

*   **Language**: Python 3
*   **Data Format**: JSON
*   **Standard Libraries**: `json`, `os`

## 🚀 Getting Started

### Prerequisites
*   Python 3.x installed on your machine.

### Installation & Usage

1.  **Clone the repository:**

2.  **Run the application:**

*(Note: Ensure the script name matches your Python file, e.g., `student_manager.py`)*

3.  **Interact with the Menu:**
The application will launch in your terminal. Simply enter the number corresponding to the action you want to perform (1-9).

## 📂 Project Structure

*   `student_manager.py`: The main application script containing all logic and the CLI menu.
*   `etudiants.json`: The data file where student records are stored (created automatically upon adding the first student).

## 📋 Menu Options

1.  **Add a student**: Input ID, name, and initialize a record.
2.  **Show students**: List all students in the database.
3.  **Search for a student**: Look up a student by their ID.
4.  **Delete a student**: Remove a student record by ID.
5.  **Add a grade**: Assign a grade (0-20) to a specific student.
6.  **Show grades**: View all grades for a specific student.
7.  **Show average**: Calculate and view a student's average and appreciation.
8.  **Class statistics**: View the overall class average and best/worst performers.
9.  **Quit**: Exit the application.