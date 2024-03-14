 # calculate grades 
def calc_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average
#student inputs

name = input("What is your name:")
class_name = input("Whats your class:")
# input grades
grade_str = input("Enter grades, seperate with spaces: ")
grade = [int(grade) for grade in grade_str.split()]
#student dict
student = {
    'name': name,
    'class_name': class_name, 
    'grades': grade
}
#
def create_student(grade, name, classes, avg):
    avg = calc_average(grade)
    return {
        'name': name,
        'classes': classes,
        'grades': grade,
        'avg': avg 

     }
# adding more students
continue_addingmore ='Y'
students_list = []

#
