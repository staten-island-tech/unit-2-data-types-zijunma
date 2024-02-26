def find_gcf(x,y):
   if x > y:
      var = y
   else:
      var = x
   for i in range(1, var + 1):
      if((x % i == 0) and (y % i == 0)):
         gcf = i
   return [gcf]

x = int(input("Your first number is:"))
y = int(input("Your second number is:"))
print ("The gcf of your numbers is:", find_gcf(x,y))

