def find_gcf(num1,num2):
    while num2: 
        num1, num2 = num2 , num1 % num2
    print([num1])

num1 = int(input("first number:"))
num2 = int(input("second number:"))

gcf = find_gcf(1,2)