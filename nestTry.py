# enter a number of q to quit

# try to change the input to a in and float, otherwise raise exception

while(True):
    try:
        value = input("Enter a number, or q to quit ")
        try:
            value = int(value) # force to an int
            break
        except:
            value = float(value) # for to a float
            break
    except:
        if(value.lower() == "q"):
            break
        else:
            print("That was not a valid input, try agian.")

# graceful close
print("Value: ", value)