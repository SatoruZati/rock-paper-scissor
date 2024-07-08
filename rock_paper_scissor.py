import random

def get_user_choice():
    # choose between rock, paper, and scissors.
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_input in ['rock', 'paper', 'scissors']:
        return user_input
    else:
        print("Invalid input. Please try again.")
        return get_user_choice()

def get_computer_choice():
    # computer's choice between rock, paper, and scissors.
    computer_choices = ['rock', 'paper', 'scissors']
    return random.choice(computer_choices)

def determine_winner(user, computer):
    # result 
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"


play_again = "yes"
user_score = 0
computer_score = 0

while play_again.lower() == "yes":
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("User chose " + user_choice + " and computer chose " +computer_choice + ".")
    winner = determine_winner(user_choice, computer_choice)
    if winner == "user":
        print("You win!")
        user_score += 1
    elif winner == "computer":
        print("Computer wins!")
        computer_score += 1
    else:
        print("It's a tie!")
    play_again = input("Do you want to play another round? (yes/no): ")
    print("\n")
print("\nThanks for playing!")
print("\nYour score is " + str(user_score) + " and computer's score is " + str(computer_score))

