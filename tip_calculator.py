# Day 2.2 exercise:
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
total_bill = float(bill)

tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage_tip = int(tip)

count = input("How many people to split the bill? ")
person_count = int(count)

contribution = (total_bill / person_count) * (1 + (percentage_tip / 100))
final_contribution = "{:.2f}".format(contribution) # formats the result to 2 decimal places

print(f"Each person should pay: ${final_contribution}")