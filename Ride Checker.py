bill = 0
height = int(input("What is your height?"))
if height > 120:
    age = int(input("What is your age?"))
    if age < 12:
        bill += 5
    elif age < 18:
        bill += 7
    elif age > 45 and age < 55:
        bill += 0
    else:
        bill += 12
    photo = str(input("Do you want a photo? Type 'Y' for YES and 'N' for NO"))
    if photo == "Y":
        bill += 3
    print (f"Your bill is ${bill}")
else:
    print ("You cannot ride.")