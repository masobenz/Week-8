"""
Name: Mason B
Date: 10/20/22
Desc: Sales management attendance; companay name, number of registers, cost per teir
"""

"""
Test Cases
attend_count = a,!,-1,0,1,2,3,4,6,9,10,15
compnay_name = alphanumeric input, alphabetic inputs, numeric input
"""

# dec val
company_name = str()
attend_count = 0 # number of attendies per company
tier_one = 150 # registering 1-3 attendies
tier_two = 100 # registering 4-9 attendies
teir_three = 90 # registering 10 or more attendies
output_value = 0 # total cost of attending

# input
company_name = str(input("What is the name of the company registering? "))

# calc
while(True):
    try:
        attend_count = int(input(f"\nHow many members will {company_name} register? "))
    except:
        print("\nThat is not a number, please try again.")
    else:
        if(attend_count <= 0):
            print("\nThat is not a valid number of attendies, please enter 1 or more.")
        else:
            break

while(True):
    if(attend_count >=1 and attend_count <= 3):
        output_value = attend_count * tier_one
    if(attend_count >= 4 and attend_count <= 9):
        output_value = attend_count * tier_two
    if(attend_count >= 10):
        output_value = attend_count * teir_three
    else:
        break        

# display
print(f"\nThat will cost {company_name} ${output_value:.00f}")


# closing