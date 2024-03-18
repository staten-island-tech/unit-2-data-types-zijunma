# Initialize the students list
students = []

# Function to calculate the average of a list of grades
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to create a new student dictionary
def create_student(name, student_class, grades):
    average_grade = calculate_average(grades)
    new_student = {
        'name': name,
        'class': student_class,
        'grades': grades,
        'average': average_grade
    }
    return new_student

# While loop to continually input new student data
continue_adding_students = "Y"
while continue_adding_students == "Y":
    student_name = input("Enter student's name: ")
    student_class = input("Enter student's class: ")
    student_grades = [int(x) for x in input("Enter student's grades separated by space: ").split()]

    new_student = create_student(student_name, student_class, student_grades)
    students.append(new_student)

    print("Student added:", new_student)

    continue_adding_students = input("Do you want to continue adding students? (Y/N): ").upper()

# Print all the students one at a time from the list
for student in students:
    print(student)

# Function to get the class average
def get_class_average(students_list):
    all_grades = [student['grades'] for student in students_list]
    flattened_grades = []
    for grades in all_grades:
        flattened_grades.extend(grades)
    class_average = calculate_average(flattened_grades)
    return class_average

# Calculate and print the class average
class_average = get_class_average(students)
print("Class Average:", class_average)
