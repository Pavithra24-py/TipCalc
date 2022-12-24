print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
tip_value = tip/100
value_bill = bill*tip_value
total = bill + value_bill
split = int(input("How many people to split the bill?"))
final = round(total / split,2)
final = "{:.2f}".format(final)
print(f"Each person should pay: {final}")



