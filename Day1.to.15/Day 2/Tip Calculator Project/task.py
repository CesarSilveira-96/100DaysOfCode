print("Welcome to the calculator!")
ttl_bill = float(input("What was the total bill? \n$"))
tip = float(input("How much tip would you like to give? 10%, 12% or 15%?\n"))
num_of_people = int(input("How many will share the bill?\n"))
bill_divided = ttl_bill / num_of_people
bill_and_tip = round(bill_divided + (bill_divided * tip/100))
print(f"Each of you will have to pay $ {bill_and_tip}")