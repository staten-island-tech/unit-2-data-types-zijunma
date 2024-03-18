student_list = []
def calculate_grades(grades):
    return sum(grades) / len(grades)


continue_addingstudents = "Y"
while continue_addingstudents == "Y":
    student_name = input("Input Student Names:")
    student_classes = input("Input Classes:")
    student_grades = [int(x) for x in input("Input Grades seperate by commas:").split()]

    student = { 
        "name": student_name,
        "classes": student_classes,
        "grades": student_grades
    }
    student['average'] = calculate_grades(student_grades)
    student_list.append(student)

    continue_addingstudents = input("Would you like to keep adding students Y/N: ")
for student in student_list:
    print("Student:", student["name"])
    print("Classes:", student["classes"])
    print("Grades:", student["grades"])
