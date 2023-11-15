import random
import copy


def guess(num):
    guess = []
    number = input(f"Enter your guess ({num} digits): ")
    while len(number) != num:
        print(f"Please enter a number {num} digits long.")
        number = input(f"Enter your guess ({num} digits): ")
    print(f"Your guess is {number}")
    for digit in number:
        guess.append(int(digit))
    return guess


class GameSetup:
    def __init__(self):
        # Initialize the secret code list
        self.secret_code = []

        # Allow duplicate colors in the secret code.
        self.num_colors = 1  # Total number of colors
        self.num_positions = 1  # Number of positions in the secret code

    def start_new_game(self):
        self.set_game_parameters()
        play_again = 'y'
        while play_again == 'y':
            hint_count = 0
            self.generate_secret_code()
            print(f"The secret code is {self.secret_code}")  # Uncomment to see the secret code
            tries = 1
            player_guess = guess(self.num_positions)
            while player_guess != self.secret_code:
                self.check_guess(player_guess)
                print("Wrong! Try again.")
                if tries % 3 == 0:
                    print('\n', '=' * 10)
                    print("Special hint offer!")
                    hint_count = self.give_hint(hint_count)
                    print('=' * 10, '\n')
                player_guess = guess(self.num_positions)
                tries += 1
            print(f"\nThe secret code was {self.secret_code}")
            if tries > 1:
                print(f"You cracked the code in {tries} tries!")
            else:
                print("You cracked the code in one try! Amazing!")
            print()
            print(f"You used {hint_count} hint/s to solve the puzzle.")
            play_again = str(input("Play again? (y/n): "))
        print("Thanks for playing!")

    def set_game_parameters(self):
        self.num_colors = int(input("Enter the number of colors (1-8): "))
        self.num_positions = int(input("Enter the number of positions (4, 6, or 8): "))
        while self.num_positions not in [4, 6, 8] or self.num_colors < 1 or self.num_colors > 8:
            if self.num_colors < 1 or self.num_colors > 8:
                print("Please choose a valid number of colors (1-8).")
                self.num_colors = int(input("Enter the number of colors (1-8): "))
            if self.num_positions not in [4, 6, 8]:
                print("Please choose a valid number of positions (4, 6, or 8).")
                self.num_positions = int(input("Enter the number of positions (4, 6, or 8): "))
        print(f"You're playing Mastermind with {self.num_colors} colors and {self.num_positions} positions.")

    def generate_secret_code(self):
        self.secret_code = []
        for _ in range(self.num_positions):
            self.secret_code.append(random.randint(1, self.num_colors))

    def check_guess(self, player_guess):
        correct_positions = 0
        # correct_colors = 0

        player_guess_copy = copy.deepcopy(player_guess)
        secret_code_copy = copy.deepcopy(self.secret_code)

        # Check for correct positions
        for i in range(len(player_guess)):
            if player_guess_copy[i] == secret_code_copy[i]:
                correct_positions += 1
                player_guess_copy[i] = -99
                # secret_code

    def give_hint(self, num_hint):
        print(f"You have used {num_hint + 1} hint/s so far.")
        give_hint = str(input("Would you like a hint? (y/n): "))
        if give_hint == 'y':
            num_hint += 1
            print("Here's a hint:")
            for i in range(num_hint):
                print(self.secret_code[i], end='')
            print()
        print("Good luck!")
        return num_hint

play_game = GameSetup()
play_game.start_new_game()
