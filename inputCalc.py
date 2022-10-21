
# from cmath import sqrt
# import math

# #dec vals
# user_input = 0.0
# calc_result = 0.0

# #prompt
# print("Welcome, let's calculate the square root of a number.")

# try:
#     user_input = int(input("Enter a number to get the square root: "))
# except:
#     print("\nThat is not a valid input, please enter a number.")
# else:
#     if user_input >= 0 or user_input <= 0:
#         calc_result = math.sqrt(user_input)
#     if user_input < 0:
#         print("Negative inputs are not a valid input. Try again.")

# print(f"\nThe square root of {user_input} is {calc_result:.0f}")

# imports
from cmath import sqrt

# decl val
user_input = 0.0
calc_value = 0.0
NameError = "nerr"

# prompt
while(True):
    try:
        user_input = int(input("Enter a number to get the square root: "))
        calc_value = cmath.sqrt(user_input)
        print(f"The square root of {user_input} is {calc_value:.0f}")
    except:
        break
    

# graceful close