a="rock"
b="paper"
c="sisor"
a>b
b>c
c>a
while True:
    player1=input("enter your option:")
    player2=input("enter your option:")
    if player1>player2:
        print(player1,"you won")
    elif player1==player2:
        print("match draw")
    else:
        print("playe2 won")
        
        break