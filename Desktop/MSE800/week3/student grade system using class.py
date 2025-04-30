class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def show_result(self):
        average = sum(self.grades) / len(self.grades) 
        result = "Passed" if average >= 60 else "Failed"
        print(f"{self.name}: {result}, Average Grade: {average:.2f}")

name = input("Enter student's name: ")
student = Student(name)

num_grades = int(input("How many subjects do you want to enter? "))
for _ in range(num_grades):
    grade = float(input("Enter grade: "))
    student.add_grade(grade)

student.show_result()

