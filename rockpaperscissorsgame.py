import random

player_score = 0
computer_score = 0

while True:
    print("\nWelcome to Rock,Paper,Scissors game")
    print("1. Play game with computer")
    print("2. Exit")
    choice = int(input("Enter your choice: "))
    if type(choice) == int and choice <= 2:
        if choice == 1:
            a = input("Rock or Paper or Scissors: ").capitalize()
            b = ["Rock", "Paper", "Scissors"]
            if a not in b:
                print("Invalid input, please enter Rock, Paper, or Scissors")
                continue
            c = random.choice(b)

            print(f"Player: {a}, Computer: {c}")

            if a == c:
                print("Draw match")
                print(f"Scores -> Player: {player_score}, Computer: {computer_score}")
            elif (
                (a == "Rock" and c == "Scissors")
                or (a == "Paper" and c == "Rock")
                or (a == "Scissors" and c == "Paper")
            ):
                print("Player wins :", a, ">", c)
                player_score += 1
                print(f"Scores -> Player: {player_score}, Computer: {computer_score}")
            # elif (
            #     (a == "Rock" and c == "Paper")
            #     or (a == "Paper" and c == "Scissors")
            #     or (a == "Scissors" and c == "Rock")
            # ):
            else:
                print("Computer wins :", c, ">", a)
                computer_score += 1
                print(f"Scores -> Player: {player_score}, Computer: {computer_score}")
            # else:
            #     print("Invalid input, please enter Rock, Paper, Scissors")
        elif choice == 2:
            print("Thanks for playing the game!!")
            print(f"Final Scores -> Player: {player_score}, Computer: {computer_score}")
            # print("Player Score :", player_score)
            # print("Computer Score :", computer_score)
            break
    else:
        print("Invalid input. Valid inputs are 1 or 2")


# import random

# player_score = 0
# computer_score = 0


# def play_game():
#     global player_score, computer_score
#     choices = ["Rock", "Paper", "Scissors"]
#     player_choice = input("Rock, Paper, or Scissors: ").capitalize()
#     if player_choice not in choices:
#         print("Invalid input, please enter Rock, Paper, or Scissors")
#         return
#     computer_choice = random.choice(choices)
#     print(f"Player: {player_choice}, Computer: {computer_choice}")

#     if player_choice == computer_choice:
#         print("Draw match")
#     elif (
#         (player_choice == "Rock" and computer_choice == "Scissors")
#         or (player_choice == "Paper" and computer_choice == "Rock")
#         or (player_choice == "Scissors" and computer_choice == "Paper")
#     ):
#         print("Player wins!")
#         player_score += 1
#     else:
#         print("Computer wins!")
#         computer_score += 1


# def main():
#     global player_score, computer_score
#     while True:
#         print("\nWelcome to Rock, Paper, Scissors game")
#         print("1. Play game with computer")
#         print("2. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             play_game()
#         elif choice == "2":
#             print("Thanks for playing the game!!")
#             print(f"Final Scores -> Player: {player_score}, Computer: {computer_score}")
#             break
#         else:
#             print("Invalid input. Valid inputs are 1 or 2")


# if __name__ == "__main__":
#     main()
