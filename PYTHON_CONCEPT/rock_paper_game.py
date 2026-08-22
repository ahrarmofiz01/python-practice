player1 = input("Player 1, enter your option: ")
player2 = input("Player 2, enter your option: ")

if player1 == player2:
    print("Match draw")

elif player1 == "rock" and player2 == "scissor":
    print("Player 1 won")

elif player1 == "scissor" and player2 == "paper":
    print("Player 1 won")

elif player1 == "paper" and player2 == "rock":
    print("Player 1 won")

elif player2 == "rock" and player1 == "scissor":
    print("Player 2 won")

elif player2 == "scissor" and player1 == "paper":
    print("Player 2 won")

elif player2 == "paper" and player1 == "rock":
    print("Player 2 won")

else:
    print("Invalid option")

    