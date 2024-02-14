def find_gcf(x,y):
   if x > y:
      variable1 = y
   else:
      variable1 = x
   for i in range(1, variable1 + 1):
      if((x % i == 0) and (y % i == 0)):
         gcf = i
   print([gcf])

x = int(input("number 1:"))
y = int(input("number 2:"))
print ("The gcf of your numbers is:")
print (find_gcf(x,y))