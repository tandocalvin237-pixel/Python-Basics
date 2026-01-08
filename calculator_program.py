# --------------------------------------------
# Simple Calculator Program in Python
# Tailored for Beginners
# --------------------------------------------

# Step 1: Print a welcome message
print("Welcome to the Python Calculator!")
print("You can perform basic operations like addition, subtraction, multiplication, division, modulus, and exponentiation.")
print("------------------------------------------------------------")

# Step 2: Explain the options to the user
print("Select the operation you want to perform:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Exponentiation (**)")
print("------------------------------------------------------------")

# Step 3: Take user input for operation choice
choice = input("Enter the number (1-6) of the operation: ")

# Step 4: Take input for numbers
# We use float() so the calculator can handle both integers and decimals
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 5: Perform calculation using if-else statements
if choice == "1":
    result = num1 + num2
    print("Result of addition:", result)

elif choice == "2":
    result = num1 - num2
    print("Result of subtraction:", result)

elif choice == "3":
    result = num1 * num2
    print("Result of multiplication:", result)

elif choice == "4":
    # Division needs error handling (cannot divide by zero)
    if num2 != 0:
        result = num1 / num2
        print("Result of division:", result)
    else:
        print("Error: Division by zero is not allowed!")

elif choice == "5":
    result = num1 % num2
    print("Result of modulus:", result)

elif choice == "6":
    result = num1 ** num2
    print("Result of exponentiation:", result)

else:
    print("Invalid choice! Please select a number between 1 and 6.")

# Step 6: End message
print("------------------------------------------------------------")
print("Thank you for using the Python Calculator!")
