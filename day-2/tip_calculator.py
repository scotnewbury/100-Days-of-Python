# Tip calculator
# input from the user - total bill
# input from the user - the tip - 10,12, or 15 percent
# input from the user - the number of people to split the bill amoung
# output - the total each person would pay

print("Welcome tto the tip calculator!")
bill_total = float(input("What was the total bill? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
party_size = int(input("How many pepole to split the bill? "))

bill_total_with_tip = bill_total * (1 + (tip_amount / 100))

print(bill_total_with_tip)

per_person_amount = round((bill_total_with_tip / party_size),2)

print(f"Each person should pay: ${per_person_amount}")