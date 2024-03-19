students_list = []


def calculate_average(grades):
    return sum(grades) / len(grades)
def createstudent(name, student_class, grades):
    average_grades = calculate_average(grades)
    new_student = {
        'Name': name,
        'Class': student_class,
        'Grades': grades,
        'Average': average_grades
    }
    return new_student
continue_addingstudents = "Y"
while continue_addingstudents == "Y":
    student_name = input("Enter student name: ")
    student_class = input("Enter student class: ")
    student_grades = [int(x) for x in input("Enter student grades seperate using commas: ").split(",")]

    new_student = createstudent(student_name, student_class, student_grades)
    students_list.append(new_student)

    continue_addingstudents = input("add more grades? : ").upper()
def get_classaverage(students_list):
    all_grades = [student['grades'] for student in students_list]
    flatten_grades = []
    for grades in all_grades:
        flatten_grades.extend(grades)
   
for student in students_list:
    print(student)
  

