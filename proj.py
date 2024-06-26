import random

while 'true':
    user_choice = input("Enter Your Choice: ")

    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors" and user_choice != "quit":
        print("Enter a proper choice")
        continue
    
    else:
        if user_choice == "quit":
            break
        else: 
            computer_choice = random.choice(["rock", "paper", "scissors"])
            print(f"Computer chose {computer_choice}")
  
            if computer_choice == user_choice:
                print("Tie")
                continue
            elif computer_choice == "rock" and user_choice == "paper":
                print("You Win")
                break
            elif computer_choice == "scissors" and user_choice == "rock":
                print("You Win")
                break
            elif computer_choice == "paper" and user_choice == "scissors":
                print("You Win")
                break
            else:
                print("You Lose. Try Again!")
                continue
