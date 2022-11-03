import json
from flask import Flask, render_template, request
import os

min_score_to_win = 5
points_player_one = 100
points_player_two = 100

game_file_name = "game_file.json"

app = Flask(__name__)

def readGameState():
    text = ''
    with open(game_file_name, 'r') as f:
        text = f.read()
        f.close()

    if text == '':
        game_state = dict()
    else:
        game_state = json.loads(text)

    return game_state

def saveGameState(game_state):
    text = json.dumps(game_state)
    with open(game_file_name, 'w') as f:
        f.write(text)
        f.close()

@app.route('/')
def index():

    return render_template('test.html')


@app.route('/test', methods=['POST'])
def test():
    game_state = readGameState()

    output = request.get_json()
    result = json.loads(output)


    if "player_one" in game_state:
        if "player_two" in game_state:

            f = open('game_file.json', 'w')
            f.write("")
            f.close()
            game_state = readGameState()

    if "player_one" in game_state:
        if "player_two" in game_state:
            print("error")

        else:
            game_state["player_two"] = {"name": result, "points": 100, "wins": 0}
    else:
        game_state["player_one"] = {"name": result, "points": 100, "wins": 0}

    saveGameState(game_state)

    return game_state

@app.route('/numbers', methods=['POST'])
def test_numbers():
    game_state = readGameState()

    output_numbers = request.get_json()
    # data = json.loads(output_numbers)

    # TODO: get from JS!
    player_name = output_numbers["name"]
    player_number = output_numbers["number"]
    print(output_numbers )
    print(game_state)

    updateNumbers(game_state, player_name, player_number)
    saveGameState(game_state)

    return game_state

@app.route('/GameStatus', methods=['GET'])
def getStatus_js():
    game_state = readGameState()
    return game_state

def updateNumbers(game_state, player_name, res_num):
    # game_state.get()

    if game_state["player_one"]["name"] == player_name:
        game_state["player_one"]["points"] -= int(res_num)
    elif game_state["player_two"]["name"] == player_name:
        game_state["player_two"]["points"] -= int(res_num)
    else:
        print("Error!!!")

def doLogic(res):
    min_score_to_win = 5

    class MyValues():
        Points = 100
        Wins = 0
        HasWon = False
        Name = ""

    GamerOne = MyValues()
    GamerTwo = MyValues()

    GamerOne.Name = res["firstplayer"]
    GamerTwo.Name = res["secondplayer"]


    def checkGameStatus():
        if GamerOne.Points > 0 and GamerTwo.Points > 0:
            return True
        else:
            return False

    def checkIfWon():
        if GamerOne.Wins < min_score_to_win and GamerTwo.Wins < min_score_to_win:
            return True
        else:
            return False

    while checkGameStatus() and checkIfWon():
        input_player_one = int(input(f"{GamerOne.Name} Enter Number:"))
        input_player_two = int(input(f"{GamerTwo.Name} Enter Number:"))

        # if input is greater than the score left reset it to the score left
        if input_player_one > GamerOne.Points:
            input_player_one = GamerOne.Points

        if input_player_two > GamerTwo.Points:
            input_player_two = GamerTwo.Points

        # repeat the game
        # make function here
        # reads file about me
        while True:
            GamerOne.Points -= input_player_one
            GamerTwo.Points -= input_player_two

            print(f"{GamerOne.Name} has left:{GamerOne.Points} points")
            print(f"{GamerTwo.Name} has left: {GamerTwo.Points} points")

            if input_player_one > input_player_two:
                GamerOne.Wins += 1
                print(f"player one won this round")

            elif input_player_one < input_player_two:
                GamerTwo.Wins += 1
                print(f"player two won this round")
            print(f"Score Player One: {GamerOne.Wins}")
            print(f"Score Player One: {GamerTwo.Wins}")

            break
        print("-------------------")
        checkGameStatus()

    # if a player reached 0 points
    # read save data
    if GamerOne.Wins >= min_score_to_win or GamerTwo.Wins >= min_score_to_win:
        if GamerOne.Wins > GamerTwo.Wins:
            print(f"player one the GAME!")
            playerOneHasWon = True
        else:
            print(f"player two the GAME!")
            playerTwoHasWon = True
    else:
        print(f"Nobody won")


