import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissor"]

while True:
    user_input = input("The Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock = 0, paper = 1, scissor = 
    computer_input = options[random_number]
    print("computer_input",computer_input + ".")
    
    if user_input == "rock" and computer_input == "scissor":    
        print("You Win!")
        user_wins += 1
    
    elif user_input == "paper" and computer_input == "rock":
        print("You win!")
        user_wins += 1
        
    elif user_input == "scissor" and computer_input == "paper":
        print("You win!")
        user_wins += 1
        
    else:
        print("You Lost!")
        computer_wins += 1
        
print("You win", user_wins,"times")
print("The Computer Win", computer_wins, "times.")
print("Goodbye!!!.")
    
        
        
        
        
    
    