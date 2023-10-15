name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on narrow road, it has come to an end and you can go left ot right. Which way would you choose to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can can walk around it or swim accross? ")
    
    if answer  == "swim":
        print("You swim accross and were eaton by an alligator.")
    elif answer == "walk":
        print("you walked for many miles, and you lost in jungle.")
    else:
        print("Not a valid option. You loss.")
        
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back.(cross/back)? ")
    
    if answer == "back":
        print("You go back and loss.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        
        if answer == "yes":
            print("You talk to stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you loss.")
        else:
            print("Not a valid option. You loss.")
    else:
        print("Not a valid option you loss.")
else:
    print("Not a valid option. You loss.")
    
        