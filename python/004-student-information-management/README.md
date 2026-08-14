# Student Information System

A simple Python Object-Oriented Programming (OOP) project that collects and manages personal information for students. The program accepts any number of students, sorts them by age, and displays their information.

## Features

* Collects student information:

  * Student ID
  * Full Name
  * Age
  * Address
* Accept the input data for the number of students according to the user input
* Uses Object-Oriented Programming (OOP)
* Stores student records using a Python list
* Sorts students by age
* Displays the sorted student information
* Includes inline comments explaining the data types used


## How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Navigate to the project directory

```bash
cd student-information-system
```

### 3. Run the Python program

```bash
python student_information.py
```

## How It Works

The program uses a `Student` class to represent each student. Each student object contains four pieces of information:

* **Student ID** – stored as a `str`
* **Full Name** – stored as a `str`
* **Age** – stored as an `int`
* **Address** – stored as a `str`

The student objects are stored in a Python `list`. This allows the program to handle any other number of students without requiring a fixed-size data structure.

After collecting the information, the program uses Python's `sorted()` function to sort the students according to their age.

## Example

```text
Student Information System
========================================
Enter the number of students: 3

Enter information for Student 1
Student ID: ST003
Full Name: John Smith
Age: 25
Address: Auckland

Enter information for Student 2
Student ID: ST001
Full Name: Mary Jones
Age: 20
Address: Wellington

Enter information for Student 3
Student ID: ST002
Full Name: David Brown
Age: 22
Address: Christchurch

Students Sorted by Age
========================================
Student ID: ST001
Full Name: Mary Jones
Age: 20
Address: Wellington
----------------------------------------
Student ID: ST002
Full Name: David Brown
Age: 22
Address: Christchurch
----------------------------------------
Student ID: ST003
Full Name: John Smith
Age: 25
Address: Auckland
----------------------------------------
```

## OOP Concepts Demonstrated

This project demonstrates basic Object-Oriented Programming concepts, including:

* **Class** – the `Student` class defines the structure of a student.
* **Object** – each student is represented as a `Student` object.
* **Constructor** – the `__init__()` method initializes student information.
* **Methods** – the `display_info()` method displays student information.
* **Encapsulation** – student information is stored within individual student objects.

## Author

Chaw Theingi

## License

This project was created for educational purposes.
