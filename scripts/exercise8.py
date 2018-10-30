stop = False
possiblePlays = ["rock", "paper", "scissors"]

while not stop:
    player1 = str(input("Rock, Paper, Scissors ? ")).lower()
    player2 = str(input("Rock, Paper, Scissors ? ")).lower()

    if(player1 not in possiblePlays or player2 not in possiblePlays):
        print('At least play Currectly')
    elif (player1 == player2):
        print('DRAW!')
    elif ((player1 == "rock" and player2 == "scissors") or
          (player1 == "paper" and player2 == "rock") or
          (player1 == "scissors" and player2 == "paper")):

        print('Player One Wins!')
    else:
        print('Player Two Wins!')

    another = str(input('Another Round?(Y/N) ')).lower()

    if another != 'y':
        stop = True
