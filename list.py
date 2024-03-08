""" accounts = [['1','2','3','4'], ["5", "6", "7"], ['1','2']]
y = [[int(i) for i in x] for x in accounts]

if (sum(y[0])) > (sum(y[1])) and (sum(y[0])) > (sum(y[2])):
    print("Customer 1 is the richest")
elif (sum(y[1])) > (sum(y[0])) and (sum(y[1])) > (sum(y[2])):
    print("Customer 2 is the richest")
else: 
    print("Customer 3 is the richest") """

def max_bank(accounts):
    max_wealth = 0 
    for customer in accounts: 
        wealth = sum(accounts)
        max_wealth = max(max_wealth, wealth)
    return wealth

accounts = [['1','2','3','4'], ["5", "6", "7"], ['1','2']]
