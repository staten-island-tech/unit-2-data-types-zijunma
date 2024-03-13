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
#average grade calcs
average_grade = calc_average(student["grades"])
#printing information

# adding more students
continue_adding_students = input("do you want to keep adding students:")
if continue_adding_students == 'Yes':
    inputingmorestudents = input("Input their names:")
    inputingmoreclasses = input("Input their classes")    
    grade_calcingformoregrades = grade_str
    