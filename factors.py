def print_factors(x):
    factors = []
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    if len(factors) == 0:
        print("Factors of 0 don't exist!")
    else: 
        print(factors)
number = int(input("Your Number Is:"))
print_factors(number)