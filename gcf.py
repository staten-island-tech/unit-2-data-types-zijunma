def find_gcf(num1,num2):
     if num1 < num2:
        num1 , num2 = num2 , num1
     while num2  !=0:
         num1 , num2 = num2 , num1 % num2
         return num1
     
num1 = int(input("First Number:"))
num2 = int(input("Second Number:"))

gcf = find_gcf(num1 , num2)
print([gcf])