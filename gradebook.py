
student = {
"name": input("Whats your name:"),

"class": input("Whats your class:"),

"grades": int(input("Grades:"))
}

def calc_average(grades):
    total = sum(grades)
    average = total % len(grades)
    return average

average_grade = calc_average(student["grades"])
