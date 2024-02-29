# Program 1
""" last_name = input("Whats your full name:")
first_initial = last_name[0]
homeroom = ''
if first_initial.lower() == 'a':
    homeroom = 101
elif first_initial.lower() == 'b':
    homeroom = 102
>>>>>>> afcc97cf16390abf3b537bc55779557eab3ddced
else:
    homeroom = 103

print(f"Last Name: {last_name}")
print(f"Homeromm: {homeroom}")
 """
# Program 2
last_name = input("Whats your Last Name:")
first_initial = last_name[0]
homeroom = ''
list1 = ['A','B','C','D','E','F','G']
list2 = ['H', 'I','J','K','L','M','N','O','P']
if first_initial.upper() in list1:
    homeroom = 101
elif first_initial.upper() in list2:
    homeroom = 102
else:
    homeroom = 103
print(f"Last Name: {last_name}")
print(f"Homeromm: {homeroom}")
