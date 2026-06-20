'''
The goal is to build a game that asks the user to guess who has more followers on Instagram.
Original Higher Lower Game
https://www.higherlowergame.com/
'''

##TODO:
# 1. import the game data from the game_data.py file
# 2. create a function that randomly selects two accounts from the game data and returns them as a tuple
# 3. create a function that takes in the two accounts and displays their names, descriptions and countries to the user
# 4. create a function that takes in the user's guess and the two accounts and returns whether the user got it right or wrong
# 5. create a function that keeps track of the user's score and displays it at the end of the game

# 1:

import random
from game_data import data
from art import logo, vs

# 2:

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

# 3:

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# 4:

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
# 5:

def play_game():
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"----------------------------------------------------------------")
            print(f"You're right! {account_a['name']} has {a_follower_count}M followers and {account_b['name']} has {b_follower_count}M followers.")
            print(f"----------------------------------------------------------------")
            print(f"Current score: {score}.")
            print(f"----------------------------------------------------------------")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. {account_a['name']} has {a_follower_count}M followers and {account_b['name']} has {b_follower_count}M followers.")
            print(f"----------------------------------------------------------------")
            print(f"Final score: {score}.")
            print(f"----------------------------------------------------------------")
            play_again = input("Do you want to play again? Type 'y' or 'n': ").lower()
            if play_again == "y":
                play_game()

# Start the game
print(logo)

play_game()
