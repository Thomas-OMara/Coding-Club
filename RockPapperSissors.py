import random


outcomes = {
    'rock': {'rock': 'draw', 'paper': 'lose', 'scissors': 'win'},
    'paper': {'rock': 'win', 'paper': 'draw', 'scissors': 'lose'},
    'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'draw'}
}


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice not in outcomes:
        return "Invalid choice. Please choose rock, paper, or scissors."
    result = outcomes[user_choice][computer_choice]
    if result == 'draw':
        return f"Both chose {user_choice}. It's a draw!"
    elif result == 'win':
        return f"You chose {user_choice} and the computer chose {computer_choice}. You win!"
    else:
        return f"You chose {user_choice} and the computer chose {computer_choice}. You lose!"


def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)


play_game()
