"""Exception handlin"""

num = int(input("enter a number"))
print("number:",num)

#w/ execption handing
try:
    num = int(input("enter another number: "))
    print("number: ",num)
except:
    print("invalid input")

#graceful close
print("\nthe program is gracefully closing")