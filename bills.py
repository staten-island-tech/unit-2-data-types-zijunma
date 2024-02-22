
bill = int(input("Bill: " ))
service = (input("service:"))
tip = 0
if service == "bad":
        tip = 0
        print("no tip")
elif service == "okay":
        tip = 0.15
        print("15% tip")
elif service == "good":
        tip = 0.20
        print("20% tip")
elif service == "great":
        tip = 0.25
        print("25% tip")
else:
        print("Invalid")

total_bill = float(bill) + (float(bill)* tip )
print(f"Total amount paid: {total_bill} dollars")
