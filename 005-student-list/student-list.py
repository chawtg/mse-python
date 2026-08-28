class Student:
    def __init__(self, full_name, age, address, student_id):
        # str is used for full name because it contains text.
        self.full_name = full_name

        # int is used for age because age is a whole number.
        self.age = age

        # str is used for address because it contains text and numbers.
        self.address = address

        # str is used for Student ID because Student ID contains letters
        # or leading zeros, for example "YB001".
        self.student_id = student_id

    def display_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Full Name: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print("-" * 40)


def main():
    # list is used to store an unknown number of Student objects.
    # It can store 70 students or any other number of students.
    students = []

    print("Student Information System")
    print("*" * 40)

    # int is used because the number of students is a whole number.
    number_of_students = int(input("Enter the number of students: "))

    for i in range(number_of_students):
        print(f"\nEnter information for Student {i + 1}")

        # str is used for text-based information.
        student_id = input("Student ID: ")
        full_name = input("Full Name: ")

        # int converts the user's input into a whole number.
        age = int(input("Age: "))

        # str is used because an address contains text.
        address = input("Address: ")

        # Create a Student object.
        student = Student(full_name, age, address, student_id)

        # Add the Student object to the list.
        students.append(student)

    # sorted() creates a new list sorted by the student's age.
    # key=lambda student: student.age tells Python to sort by age.
    sorted_students = sorted(students, key=lambda student: student.age)

    print("\nStudents Sorted by Age")
    print("*" * 40)

    # Display the sorted students.
    for student in sorted_students:
        student.display_info()


# Start the program.
if __name__ == "__main__":
    main()