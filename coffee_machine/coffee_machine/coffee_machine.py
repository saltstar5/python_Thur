coinprint  = {0.25:"How many quarters? : ",
              0.1:"How many dimes? : ",
              0.05:"How many nicles? : ",
              0.01:"How many pennies? : "}

menutable = {"espresso":[1.50,50,18,0],
             "latte":[2.50,200,24,150],
             "cappuccino":[3.00,250,24,100]
            }

Inventory = {"Money":[0,"$"],
             "Water":[300,"ml"],
             "Coffee":[100,"g"],
             "Milk":[200,"ml"]
            }

def print_report():
    for key, values in Inventory.items():
        if key=='Money':
            print(f"{key} : {values[1]} {values[0]}")
        else:
            print(f"{key} : {values[0]} {values[1]}")

def control_resources(order):
    i=0
    for key, values in Inventory.items():
        if i>0 and Inventory[key][0]<menutable[order][i]:
            return i
        i+=1
    return 0

def control_coins(order):
    sum=0
    for key,values in coinprint.items():
        sum+= (key*float(input(values)))
    if sum > menutable[order][0]:
        charge = sum-menutable[order][0]
        print(f"Here is ${charge} dollars in charge.")
    elif sum < menutable[order][0]:
        print("Sorry that's not enough money. Money refunded")
        return False
    return True


def make_coffee(order):
    i=0
    for key, values in Inventory.items():
        if key=='Money':
            Inventory[key][0]+=menutable[order][i]
        else:
            Inventory[key][0]-=menutable[order][i]
        i+=1

    return True


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'report':
        print_report()
    elif order =='off':
        break
    else:
        ## check resources
        result=control_resources(order)
        if result>0:
            temp = list(Inventory.keys())
            print(f"Sorry there is not enough {temp[result]}")
        else:
            print("Please insert coins.")
            if control_coins(order): ## control coin
                make_coffee(order) ## make coffee