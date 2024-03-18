def calculate_grades(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

student = { 
    'name': '',
    'class': '', 
    'grade': '', 
}

def createnewstudent(name, classes, grade):
    avg_grades = calculate_grades(grade)
    return { 
        'name': name, 
        'class': classes, 
        'grades': grade,
        'average': avg_grades 
    }
def zijun_idiot():

    continue_makingstudents = input("Y")
    student_list = []

    while continue_makingstudents == "Y":
        student_name = input("Enter the name:")
        student_class = input("Enter your class:")
        student_grades = input("Enter grades separated with commas:").split(',')
        student_grades = [int(grade) for grade in student_grades]

        new_student = createnewstudent(student_name, student_class, student_grades)
        student_list.append(new_student)

    for student in student_list:
        print("Name:", student["name"])
        print("Class:", student["class"])
        print("Grades:", student["grades"])
        print("Average:", student["average"])
        print()

continue_makingstudents = input("Do you want to keep adding more students:")
print("Program has ended")
