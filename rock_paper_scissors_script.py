import random

list = ["rock", "paper", "scissors"]

# Get user input
player_score = 0
computer_score = 0

while True:
    
    while True:
        user_choice = input("Welcome to Rock, Paper, Scissors! Select rock, paper, or scissors to begin: ").strip().lower()   # Normalize input (remove spaces and convert to lowercase)
        # Check if the input is in the list
        if user_choice in list:
            print("Valid input!")
            print("Great, you chose: " + user_choice)
            break
        else:
            print("Wrong input! Please try again.")
            
    # Computer choice
    computer_choice = random.choice(list)
    print(f"Computer chose: {computer_choice}")
    

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        player_score += 1
        print(f"You win! The computer choose {computer_choice}. Rock beats scissors.")
    elif user_choice == "paper" and computer_choice == "rock":
        player_score += 1
        print(f"You win! The computer choose {computer_choice}. Paper beats rock.")
    elif user_choice == "scissors" and computer_choice == "papper":
        player_score += 1   
        print(f"You win! The computer choose {computer_choice}. Scissors beats papper.")
    elif user_choice == "rock" and computer_choice == "paper":
        computer_score += 1
        print(f"You lose! The computer choose {computer_choice}. Rock beats paper.")
    elif user_choice == "paper" and computer_choice == "scissors":
        computer_score += 1
        print(f"You lose! The computer choose {computer_choice}. Paper beats scissors.")
    elif user_choice == "scissors" and computer_choice == "rock":
        computer_score += 1
        print(f"You lose! The computer choose {computer_choice}. Scissors beats rock.")
    
    # Display the score
    print("Player score: " + str(player_score) + " Computer score: " + str(computer_score))

    # Ask the user if they want to play again
    while True:
        play_again = input("Would you like to play again? (y/n):").strip().lower()
        if play_again == "n":
                print("Thanks for playing!")
                exit()
        elif play_again == "y":
                break
        else:
                print("Invalid input. Please try again.")

        
