
student = {
    'name': "Sidh Gupta",
    'class': "101",
    'grades':[90, 86, 76]
}

def calc_average(grades):
    total = sum(grades)
    average = total % len(grades)
    return average

average_grade = calc_average(student["grades"])
