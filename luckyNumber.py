"""
Name: Mason B
Date: 10/18/22
Desc: Prompt for lucky number, display results
"""

# decl vars
# from random import random


# lucky_num = 0

# # prompt number, if not valid assign a number
# try:
#     lucky_num = int(input("Enter your lucky number: "))
# except:
#     print("Invalid input, you will be assigned a lucky number")
#     # assign a random number
#     lucky_num = int(random()*10)

# # display results
# # Your lucky number is 19
# print(f"Your lucky number is {lucky_num}")

# # more lucky numbers (0-99)
# print("More lucky numbers")
# for count in range(12):
#     print(int(random()*100))

# lucky number in some range
# otherRange = min + (random() * (max - min))

from random import randrange


print("Lucky number between 35 and 55")
for count in range(20):
    print(randrange(35,55))