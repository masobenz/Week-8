# multiple exceptions

try:
    number = int(input("Enter a number: "))
    answer = 5 / number

    #NameError
    if(number == 60):
        print("5 / 60 = 0.08")
except ValueError:
    print("\nThat is not a number")
except ZeroDivisionError as err:
    print(err)

# graceful close
print("\nThe program is closing")
