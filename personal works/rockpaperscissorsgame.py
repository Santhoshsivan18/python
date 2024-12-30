import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Global variables for scores
player_score = 0
computer_score = 0


class MainApp:
    def __init__(s, root):
        s.root = root
        s.root.title("Rock, Paper, Scissors Game")

        # Load images
        s.rock_image = ImageTk.PhotoImage(
            Image.open("rock.png").resize((150, 150), Image.LANCZOS)
        )
        s.paper_image = ImageTk.PhotoImage(
            Image.open("paper.png").resize((150, 150), Image.LANCZOS)
        )
        s.scissors_image = ImageTk.PhotoImage(
            Image.open("scissors.png").resize((150, 150), Image.LANCZOS)
        )

        # Create buttons with images
        s.rock_button = tk.Button(
            root, image=s.rock_image, command=lambda: s.play_game("Rock")
        )
        # s.rock_button.pack(side=tk.LEFT, padx=10, pady=20)
        s.rock_button.grid(row=0, column=0)

        s.paper_button = tk.Button(
            root, image=s.paper_image, command=lambda: s.play_game("Paper")
        )
        # s.paper_button.pack(side=tk.LEFT, padx=10, pady=20)
        s.paper_button.grid(row=0, column=1)

        s.scissors_button = tk.Button(
            root, image=s.scissors_image, command=lambda: s.play_game("Scissors")
        )
        # s.scissors_button.pack(side=tk.LEFT, padx=10, pady=20)
        s.scissors_button.grid(row=0, column=2)

        # Label to display scores
        s.score_label = tk.Label(
            root, text=f"Player: {player_score} Computer: {computer_score}"
        )
        s.score_label.grid(row=1, column=1)

        # Initialize result label with empty text
        s.result_label = tk.Label(root, text="")
        s.result_label.grid(row=2, column=0, columnspan=3)

    def play_game(s, player_choice):
        global player_score, computer_score
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "Draw match"
        elif (
            (player_choice == "Rock" and computer_choice == "Scissors")
            or (player_choice == "Paper" and computer_choice == "Rock")
            or (player_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "Player wins!"
            player_score += 1
        else:
            result = "Computer wins!"
            computer_score += 1

        # Update result label with the game's outcome
        s.result_label.config(
            text=f"Choices: Player: {player_choice} Computer: {computer_choice}\nResult: {result}"
        )
        # Update score label
        s.score_label.config(text=f"Player: {player_score} Computer: {computer_score}")

        # Update result label
        # choice_label.config(text=result)
        # Update score label
        # s.score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")
        # messagebox.showinfo("Result", result)


def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()


# import random

# player_score = 0
# computer_score = 0

# while True:
#     print("\nWelcome to Rock,Paper,Scissors game")
#     print("1. Play game with computer")
#     print("2. Exit")
#     choice = int(input("Enter your choice: "))
#     if type(choice) == int and choice <= 2:
#         if choice == 1:
#             a = input("Rock or Paper or Scissors: ").capitalize()
#             b = ["Rock", "Paper", "Scissors"]
#             if a not in b:
#                 print("Invalid input, please enter Rock, Paper, or Scissors")
#                 continue
#             c = random.choice(b)

#             print(f"Player: {a}, Computer: {c}")

#             if a == c:
#                 print("Draw match")
#                 print(f"Scores -> Player: {player_score}, Computer: {computer_score}")
#             elif (
#                 (a == "Rock" and c == "Scissors")
#                 or (a == "Paper" and c == "Rock")
#                 or (a == "Scissors" and c == "Paper")
#             ):
#                 print("Player wins :", a, ">", c)
#                 player_score += 1
#                 print(f"Scores -> Player: {player_score}, Computer: {computer_score}")
#             # elif (
#             #     (a == "Rock" and c == "Paper")
#             #     or (a == "Paper" and c == "Scissors")
#             #     or (a == "Scissors" and c == "Rock")
#             # ):
#             else:
#                 print("Computer wins :", c, ">", a)
#                 computer_score += 1
#                 print(f"Scores -> Player: {player_score}, Computer: {computer_score}")
#             # else:
#             #     print("Invalid input, please enter Rock, Paper, Scissors")
#         elif choice == 2:
#             print("Thanks for playing the game!!")
#             print(f"Final Scores -> Player: {player_score}, Computer: {computer_score}")
#             # print("Player Score :", player_score)
#             # print("Computer Score :", computer_score)
#             break
#     else:
#         print("Invalid input. Valid inputs are 1 or 2")
