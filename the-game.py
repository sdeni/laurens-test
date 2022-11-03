points_player_one = 100
points_player_two = 100

player_one_wins = 0
player_two_wins = 0

min_score_to_win = 2

playerOneHasWon = False
playerTwoHasWon = False

def checkGameStatus():
    if points_player_one > 0 and points_player_two > 0 and player_one_wins < min_score_to_win and player_two_wins < min_score_to_win:
        return True
    else:
        return False
# as long the players have points PLAY!
while checkGameStatus():
    input_player_one = int(input("Enter a number to play with one"))
    input_player_two = int(input("Enter a number to play with two"))

# if input is greater than the score left reset it to the score left
    if input_player_one > points_player_one:
        input_player_one = points_player_one

    if input_player_two > points_player_two:
        input_player_two = points_player_two

# repeat the game
    while True:
        points_player_one -= input_player_one
        points_player_two -= input_player_two

        print(f"One has left:{points_player_one}")
        print(f"two has left: {points_player_two}")

        if input_player_one > input_player_two:
            player_one_wins += 1
            print(f"player one won this round")

        elif input_player_one < input_player_two:
            player_two_wins += 1
            print(f"player two won this round")
        print(f"Score Player One: {player_one_wins}")
        print(f"Score Player One: {player_two_wins}")

        break
    print("-------------------")
    checkGameStatus()

# if a player reached 0 points
if player_one_wins >= min_score_to_win or player_two_wins >= min_score_to_win:
    if player_one_wins > player_two_wins:
        print(f"player one the GAME!")
        playerOneHasWon = True
    else:
        print(f"player two the GAME!")
        playerTwoHasWon = True
else:
    print(f"Nobody won")




