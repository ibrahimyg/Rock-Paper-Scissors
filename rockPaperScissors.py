import random
exit = False

while exit == False:
    list = ["rock", "paper", "scissors"]
    computerSelection = random.choice(list)
    userSelection = input("Rock, Paper, Scissor: ")

    if userSelection == "paper":
        if computerSelection == "rock":
            print("User won, computer chosed", computerSelection)
        elif computerSelection == "paper":
            print("Tie, computer chosed", computerSelection)
        elif computerSelection == "scissor":
            print("User lost, computer chosed", computerSelection)
    elif userSelection == "rock":
        if computerSelection == "rock":
            print("Tie, computer chosed", computerSelection)
        elif computerSelection == "paper":
            print("User lost, computer chosed", computerSelection)
        elif computerSelection == "scissor":
            print("User won, computer chosed", computerSelection)
    elif userSelection == "scissor":
        if computerSelection == "rock":
            print("User lost, computer chosed", computerSelection)
        elif computerSelection == "paper":
            print("User won, computer chosed", computerSelection)
        elif computerSelection == "scissor":
            print("Tie, computer chosed", computerSelection)