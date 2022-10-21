# force valid input

# from operator import truediv


# try:
#     num = int(input("Enter a number: "))
# except:
#     print("Invalid input, that was not a number")

# # force the input
# print()
# valid = False
# while(not valid):
#     try:
#         valid = True # reset the flag
#         num = int(input("Enter another number: "))
#         print("Number: ", num)
#     except:
#         print("Another invalid input, try again.")
#         valid = False

# # shortcut
# print("\n")
# while(True):
#     try:
#         num = float(input("Enter a floating point number: "))
#         print("Number: ",num)
#         break # break out of the loop
#     except:
#         print("That is not a valid number")

# force a range
print("\n")
while(True):
    try:
        num = int(input("Enter a number between 1 and 15: "))
    except:
        print("That is not a number, try again.")
    else:
        if(num < 1 or num > 15):
            print("That number is not in range, try again.")
        else:
            print("The number is: ", num)
            break # break out of loop

# force number > 0
# num = 0
# while(True):
#     try:
#         num = int(input("Enter a number greater than zero: "))
#     except:
#         print("Invalid input")
#     if(num > 0):
#         break # break out of loop

# print("The number is: ", num)

#graceful close
print("\nThe program is gracefully closing")