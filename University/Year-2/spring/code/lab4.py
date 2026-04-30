choices = ["rock", "paper", "scissors"]


def computer_pick(current_round):
    """
    Pick rock if current_round is a multiple of 3, i.e., 0, 3, 6, 9 ...
    Pick paper if current_round is 1 or 4 or 7, ....
    Pick scissors otherwise

    Hints:
    1. current_round % 3 == 0 to check if it is a multiple of 3
    current_round % 3 == 1 to see if current_round is 1 or 4 or 7, ....

    2. This function needs to return a string which is either rock or paper or scissors
    For that you can use
    return "rock"  # computer chooses rock
    return "paper" # computer chooses paper
    return "scissors" # computer chooses scissors
    """
    if current_round % 3 == 0:
        return "rock"
    elif current_round % 3 == 1:
        return "paper"
    else:
        return "scissors"


def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif computer_choice == "rock" and player_choice == "paper":
        return "player"
    elif computer_choice == "rock" and player_choice == "scissors":
        return "computer"
    elif computer_choice == "paper" and player_choice == "scissors":
        return "player"
    elif computer_choice == "paper" and player_choice == "rock":
        return "computer"
    elif computer_choice == "scissors" and player_choice == "rock":
        return "player"
    elif computer_choice == "scissors" and player_choice == "paper":
        return "computer"


def update_scores(scores, winner):
    if winner == "player":
        scores[0] += 1
    elif winner == "computer":
        scores[1] += 1


def play_rps():
    current_round = 0
    max_rounds = 6
    scores = [0, 0]

    while current_round < max_rounds:
        player_choice = input("Enter rock, paper, or scissors (or quit to exit): ")

        if player_choice == "quit":
            break

        if player_choice not in choices:
            print("Invalid choice!")
            continue

        computer_choice = computer_pick(current_round)

        # Check who wins
        result = check_winner(player_choice, computer_choice)
        update_scores(scores, result)

        # Display result
        print("You chose:", player_choice, "Computer chose:", computer_choice)
        print("Result:", result)
        print("Scores - You:", scores[0], "Computer:", scores[1])

        current_round += 1


play_rps()
