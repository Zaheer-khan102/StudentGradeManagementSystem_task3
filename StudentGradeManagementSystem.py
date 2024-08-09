class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.calculate_average()}")


def main():
    students = {}

    while True:
        print("\n1. Add Student")
        print("2. Add Grade")
        print("3. Display Student Info")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            name = input("Enter student name: ")
            students[name] = Student(name)
            print("Student added successfully.")
        elif choice == 2:
            name = input("Enter student name: ")
            if name in students:
                grade = float(input("Enter grade: "))
                students[name].add_grade(grade)
                print("Grade added successfully.")
            else:
                print("Student not found.")
        elif choice == 3:
            name = input("Enter student name: ")
            if name in students:
                students[name].display_info()
            else:
                print("Student not found.")
        elif choice == 4:
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()