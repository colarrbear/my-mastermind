# import random
# import copy


# def guess(num):
#     guess = []
#     number = input(f"Enter your guess ({num} digits): ")
#     while len(number) != num:
#         print(f"Please enter a number {num} digits long.")
#         number = input(f"Enter your guess ({num} digits): ")
#     print(f"Your guess is {number}")
#     for digit in number:
#         guess.append(int(digit))
#     return guess


# class GameSetup:
#     def __init__(self):
#         # Initialize the secret code list
#         self.secret_code = []

#         # Allow duplicate colors in the secret code.
#         self.num_colors = 1  # Total number of colors
#         self.num_positions = 1  # Number of positions in the secret code

#     def start_new_game(self):
#         self.set_game_parameters()
#         play_again = 'y'
#         while play_again == 'y':
#             hint_count = 0
#             self.generate_secret_code()
#             print(f"The secret code is {self.secret_code}")  # Uncomment to see the secret code
#             tries = 1
#             player_guess = guess(self.num_positions)
#             while player_guess != self.secret_code:
#                 self.check_guess(player_guess)
#                 print("Wrong! Try again.")
#                 if tries % 3 == 0:
#                     print('\n', '=' * 10)
#                     print("Special hint offer!")
#                     hint_count = self.give_hint(hint_count)
#                     print('=' * 10, '\n')
#                 player_guess = guess(self.num_positions)
#                 tries += 1
#             print(f"\nThe secret code was {self.secret_code}")
#             if tries > 1:
#                 print(f"You cracked the code in {tries} tries!")
#             else:
#                 print("You cracked the code in one try! Amazing!")
#             print()
#             print(f"You used {hint_count} hint/s to solve the puzzle.")
#             play_again = str(input("Play again? (y/n): "))
#         print("Thanks for playing!")

#     def set_game_parameters(self):
#         self.num_colors = int(input("Enter the number of colors (1-8): "))
#         self.num_positions = int(input("Enter the number of positions (4, 6, or 8): "))
#         while self.num_positions not in [4, 6, 8] or self.num_colors < 1 or self.num_colors > 8:
#             if self.num_colors < 1 or self.num_colors > 8:
#                 print("Please choose a valid number of colors (1-8).")
#                 self.num_colors = int(input("Enter the number of colors (1-8): "))
#             if self.num_positions not in [4, 6, 8]:
#                 print("Please choose a valid number of positions (4, 6, or 8).")
#                 self.num_positions = int(input("Enter the number of positions (4, 6, or 8): "))
#         print(f"You're playing Mastermind with {self.num_colors} colors and {self.num_positions} positions.")

#     def generate_secret_code(self):
#         self.secret_code = []
#         for _ in range(self.num_positions):
#             self.secret_code.append(random.randint(1, self.num_colors))

#     def check_guess(self, player_guess):
#         correct_positions = 0
#         # correct_colors = 0

#         player_guess_copy = copy.deepcopy(player_guess)
#         secret_code_copy = copy.deepcopy(self.secret_code)

#         # Check for correct positions
#         for i in range(len(player_guess)):
#             if player_guess_copy[i] == secret_code_copy[i]:
#                 correct_positions += 1
#                 player_guess_copy[i] = -99
#                 # secret_code

#     def give_hint(self, num_hint):
#         print(f"You have used {num_hint + 1} hint/s so far.")
#         give_hint = str(input("Would you like a hint? (y/n): "))
#         if give_hint == 'y':
#             num_hint += 1
#             print("Here's a hint:")
#             for i in range(num_hint):
#                 print(self.secret_code[i], end='')
#             print()
#         print("Good luck!")
#         return num_hint

# play_game = GameSetup()
# play_game.start_new_game()

class MasterMind:

    def __get_puzzle(self, num_color, num_pos):
        import random
        answer = ''

        for i in range(0, num_pos):
            x = random.randint(1, num_color)
            answer += str(x)
        return str(answer)
    
    def __sanitize_input(self, num_color, num_pos):
        try:
            x = int(num_color)
        except ValueError:
            print(num_color, ": not valid as a value for number for colors")

        if x < 0:
            x = 1
        elif x > 8:
            x = 8

        try:
            y = int(num_pos)
        except ValueError:
            print(num_pos, ": not valid as a value for number of postions")
        
        if y < 0:
            y = 1
        elif y > 10:
            y = 10
        
        return [x, y]

    def __init__(self, num_color, num_pos):
        [self.num_color, self.num_pos] = self.__sanitize_input(num_color, num_pos)
        self.puzzle = self.__get_puzzle(self.num_color, self.num_pos)
        self.ans_list = []
        self.game_end = False

    def __get_clue(self, guess, ans):
        black = 0
        ans_list = list(ans)
        orig_len = len(ans_list)
        for i in range(len(guess)):
            if guess[i] == ans[i]:
                black += 1
        for char in guess:
            if char in ans_list:
                ans_list.remove(char)
        white = orig_len - len(ans_list)
        white -= black
        return [black, white]
    
    def __str_clue(self, hint):
        s = ""
        for i in range(0, hint[0]):
            s += '* '
        for i in range(0, hint[1]):
            s += 'o '
        return s[0:-1]

    def play(self):
        print("Here is the puzzle:", self.puzzle)
        print("Playing MM with", self.num_color, "colors and", self.num_pos, "positions")
        while (not self.game_end):
            print("What is your guess?: ", end='')
            your_try = input()
            print("Your guess is", your_try[0:self.num_pos])
            hint = self.__get_clue(your_try[0:self.num_pos], self.puzzle)
            print(self.__str_clue(hint))
            print()
            self.ans_list.append([your_try, hint])
            if hint[0] == self.num_pos:
                self.game_end = True
                print("You solve the puzzle after", len(self.ans_list), "rounds")
    
    def summarize(self):
        if not self.game_end:
            return
        for item in self.ans_list:
            print(item[0], self.__str_clue(item[1]))
    
my_game = MasterMind(10, 20)
my_game.play()
my_game.summarize()
