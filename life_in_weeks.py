# Day 2.1 exercise:
# Create a program using maths anf f-Strings that tell us how many
# days, weeks, months we have left if we live until 90 years old.

# Don't change the code below
age = input("What is your current age? ")
# Don't change the code above

# Write your code below this line
years_left = 90 - int(age)
days_left = 365 * years_left
weeks_left = 52 * years_left
months_left = 12 * years_left

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)