bill = (input("Bill: "))
Service = (input("Service: "))
if Service == "bad":
        tip = 0
        print("no tip")
elif Service == "okay":
        tip = 0.15
        print("15% tip")
elif Service == "good":
        tip = 0.20
        print("20% tip")
elif Service == "great":
        tip = 0.25
        print("25% tip")
else:
        print("Invalid")

total_bill = float(bill) + (float(bill)* tip )
print(f"Total amount paid: {total_bill}")