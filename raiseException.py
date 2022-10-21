# raise our own exception

#generic exception
try:
    age = int(input("how old are you?"))
    if(age<0):
        raise Exception()
except:
    print("Wait... you can't be less than zero years old")

#specific exception
try:
    name = input("What is your name? Don't say Voldemort: ")
    if(name.lower() == "voldemort"):
        raise NameError("Didn't I say, don't say that name!")
except NameError as err:
    print(err)
    print("Better luck next time")

print("Be cardful of continuing without forcing valid input,", name)