
student = {
    'name': "Sidh Gupta",
    'class': "101",
    'grades':[50,60,60]
}

def calc_average(grades):
    total = sum(grades)
    average = total % len(grades)
    return average

average_grade = calc_average(student["grades"])
print("Your average is:", average_grade)
