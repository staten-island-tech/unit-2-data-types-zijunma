# Program 1
""" last_name = input("Whats your full name:")
first_initial = last_name[0]
homeroom = ''

if first_initial.lower() == 'a':
    homeroom = 101
elif first_initial.lower() == 'b':
    homeroom = 102
else:
    homeroom = 103

print(f"Last Name: {last_name}")
print(f"Homeromm: {homeroom}")
 """
# Program 2
last_name = input("Whats your full name:")
first_initial = last_name[0]
homeroom = ''

if first_initial.lower() in 'abcdefgh':
    homeroom = 101
elif first_initial.lower() in 'ijklmnop':
    homeroom = 102
else:
    homeroom = 103

print(f"Last Name: {last_name}")
print(f"Homeromm: {homeroom}")