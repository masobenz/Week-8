"""
Name: Mason B
Date: 10/18
Desc: Prompt for customer package weight"""

# decl vals
package_weight = 0
cost_per_pound = 0.00
total_cost = 0.00

# range 0.2 - 65.75 lbs
while(True):
    try: 
        package_weight = float(input("Enter the weight of your package, between 0.2 and 65.75 pounds: "))
    except:
        print("Invalid input, try agian.") 
    else:
        if(package_weight < 0.2 and package_weight > 65.75):
            print("That is not within range")
        break
     
# calc cost $0.27 per pound
cost_per_pound = 0.27
total_cost = package_weight * cost_per_pound
print(f"Your total cost to ship your {package_weight} pound package, will be ${total_cost:.00f}")

# display results w/ graceful close
print("\nHappy shipping!")