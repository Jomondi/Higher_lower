import random
from game_data import data
from art import logo, vs

wanna_play = input("Would you like to play some high-low? Type 'yes' or 'no': ").lower()


def high_low():
    # wanna_play = input("Would you like to play some high-low? Type 'yes' or 'no': ").lower()
    if wanna_play == "yes":
        game_over = False
        print(logo)
        A = random.choice(data)
        print(f"\nCompare A: {A['name']}, a {A['description']}, from {A['country']}.")
        print(vs)
        B = random.choice(data)
        print(f"\nCompare B: {B['name']}, a {B['description']}, from {B['country']}.\n")

        while not game_over:
            more_followers = input("Who has more followers? Type 'A' or 'B': ")
            if more_followers == 'A' and (A["follower_count"] > B["follower_count"]):
                A = A
                B = random.choice(data)
                print("\n--------------------------------------------------------------------------------")
                print(f"\nCompare A: {A['name']}, a {A['description']}, from {A['country']}.")
                print(f"\nCompare B: {B['name']}, a {B['description']}, from {B['country']}.\n")
                game_over = False
            elif more_followers == 'B' and (A["follower_count"] > B["follower_count"]):
                game_over = True
            elif more_followers == 'B' and (A["follower_count"] < B["follower_count"]):
                A = B
                B = random.choice(data)
                print("\n--------------------------------------------------------------------------------")
                print(f"\nCompare A: {A['name']}, a {A['description']}, from {A['country']}.")
                print(f"\nCompare B: {B['name']}, a {B['description']}, from {B['country']}.\n")
                game_over = False
            elif (more_followers == 'A' or more_followers == 'B') and (A["follower_count"] == B["follower_count"]):
                A = B
                B = random
                print("\n--------------------------------------------------------------------------------")
                print(f"\nCompare A: {A['name']}, a {A['description']}, from {A['country']}.")
                print(f"\nCompare B: {B['name']}, a {B['description']}, from {B['country']}.\n")
                game_over = False
            else:
                game_over = True

    else:
        exit("Thanks for coming. Goodbye....")


def play_again():
    print("\n--------------------------------------------------------------------------------")
    go_again = input("\nWould you like to go again? Type 'yes' or 'no': ").lower()
    if go_again == 'yes':
        high_low()
    else:
        exit("Thanks for coming. Goodbye ")


high_low()
play_again()
