#this simple program is one that does the following things:
# •	Stores personal data using variables
# o	Name (string)
# o	Age (integer)
# o	Height in meters (float)
# o	Is enrolled (boolean)
# •	Calculates:
# o	Age in months
# o	Height in centimeters
# •	Compares:
# o	Age to a minimum age requirement (e.g., 18)
# •	Prints a clean, readable summary

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
fullname = f"{fname} {lname}"
height_in_centimeters = float(input("Enter your height in centimeters: "))
birth_year = int(input("Enter your birth year: "))



height_in_meters = height_in_centimeters * 100
age_in_months = ((2026-birth_year)*12) + 1
age_in_years = 2025-birth_year

if age_in_months <= 18:
    enrolled = False

else:
    enrolled = True

print(" Wellcome to RAVVLE In, Here is your information: ".center(60, "="))
print("Your name: ".ljust(20, "."), fullname.rjust(40, "."))
print("Your age: ".ljust(30, "."), str(age_in_years).rjust(30, "."))
print("Your height in meters: ".ljust(30, "."), str(height_in_meters).rjust(30, "."))
print("Your age in months: ".ljust(30, "."), str(age_in_months).rjust(30, "."))
print("")

if enrolled:
    print("Since you are more than 18 years old,\nEnrollment successful")

else:
    print("Since you are less than 18 years old,\nEnrollment unsuccessful")







