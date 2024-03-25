#student list
students_list = []
def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)
def createstudent(name, student_class, grades):
    average_grades = calculate_average(grades)
    new_student = {
        'Name': name,
        'Class': student_class,
        'Grades': grades,
        'Average': average_grades
    }
    return new_student
#adding students 
continue_addingstudents = "Y"
while continue_addingstudents == "Y":
    student_name = input("Enter student name: ")
    student_class = input("Enter student class: ")
    student_grades = [int(x) for x in input("Enter student grades seperate using commas: ").split(",")]
#creates students
    new_student = createstudent(student_name, student_class, student_grades)
    students_list.append(new_student)
    continue_addingstudents = input("Add more grades? : ").upper()
#prints the information 
for student in students_list:
    print(student)
#find class average
all_grades = [grade for student in students_list for grade in student['Grades']]
class_average = calculate_average(all_grades)
print("Class Average is:", class_average)
