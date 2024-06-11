# Lesson 2: The Magic of Conditional Statements: Assignments: Dive Deeper

# 1. Decisions at the Crossroad
# number = int(input("Enter a number"))

# if number > 0:
#     print("The number is positive.")
# elif number == 0:
#     print("The number is zero.")
# else:
#     print("The number is negative.")

# 2. The Greatest Showdown
number1 = int(input("Enter 1st number"))
number2 = int(input("Enter 2nd number"))
number3 = int(input("Enter 3rd number"))

if (number1 >= number2) and (number1 >= number3):
    largest = number1
elif (number2 >= number1) and (number2 >= number3):
    largest = number2
else:
    largest = number3
print(f"The biggest number is {largest}")


