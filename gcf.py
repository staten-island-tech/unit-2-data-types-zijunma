def find_gcf(num1,num2):
     if num1 < num2:
        num1 , num2 = num2 , num1
     while num2  !=0:
        temp = num2
        num2 = num1 % num2
        num1 = temp 

print (["num1"])

num1 = (input("First Number:"))
num2 = (input("Second Number:"))