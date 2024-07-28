#Project 2: Tax Bracket Calculator

income = int(input("Please enter the income: "))
age = int(input("Please enter the age of the citizen: "))
crimrecord = str(input("Does the citizen have a criminal record (yes/no): "))

if (income >= 100000 and age >= 65):
    tax = income * 0.20
elif (income >= 100000):
    tax = income * 0.25
elif (income >= 75000):
    tax = income * 0.19
elif (income >= 50000):
    tax = income * 0.14
elif (income >= 25000):
    tax = income * 0.10
else:
    tax = income * 0.08

crimrecord = crimrecord.casefold()
if (crimrecord == "yes"):
    tax +=(tax*0.10)

print("The tax amount is $" + str(int(tax)))
