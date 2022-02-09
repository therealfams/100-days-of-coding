print("---Welcome to tip calculator---")

total_bill = float(input("What was the total bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15 "))
split = int(input("How many people will split the bill "))
bill = round((((tip_percentage / 100) * total_bill) + total_bill) / split , 2)

print(f"Each person should pay {bill}")
 
    