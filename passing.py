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
            game_state["player_two"] = {"name": result, "points": 100, "wins": 0, "current_input": 0,
                                        "EnteredNumber": False, "GameIsOn": True, "HasWon": False}
    else:
        game_state["player_one"] = {"name": result, "points": 100, "wins": 0, "current_input": 0,
                                    "EnteredNumber": False, "GameIsOn": True, "HasWon": False}

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
    player_current_input = output_numbers["number"]
    print(output_numbers)
    print(game_state)

    updateNumbers(game_state, player_name, player_number, player_current_input)
    saveGameState(game_state)

    return game_state


@app.route('/GameStatus', methods=['GET'])
def getStatus_js():
    game_state = readGameState()
    return game_state


def updateNumbers(game_state, player_name, res_num, player_current_input):
    # game_state.get()

    # check if both have entered an change to false
    if game_state["player_one"]["EnteredNumber"] == True and game_state["player_two"]["EnteredNumber"] == True:
        game_state["player_one"]["EnteredNumber"] = False
        game_state["player_two"]["EnteredNumber"] = False


    if game_state["player_one"]["name"] == player_name:
        points_p1 = game_state["player_one"]["points"]
        # if player has 4/5 ad enouh points to win rithzrt way then its already won

        if points_p1 == 0:
            print("Game Over P1")
            return
        if not game_state["player_one"]["EnteredNumber"]:
            if points_p1 - int(player_current_input) > 0:
                game_state["player_one"]["points"] -= int(res_num)
                game_state["player_one"]["current_input"] = player_current_input
                game_state["player_one"]["EnteredNumber"] = True
                checkWinner(game_state)
            else:
                game_state["player_one"]["current_input"] = game_state["player_one"]["points"]
                game_state["player_one"]["points"] = 0
                game_state["player_one"]["EnteredNumber"] = True
                game_state["player_one"]["GameIsOn"] = False
                checkWinner(game_state)

    elif game_state["player_two"]["name"] == player_name:
        if game_state["player_two"]["points"] == 0:
            print("Game Over P1")
            return
        if not game_state["player_two"]["EnteredNumber"]:
            if game_state["player_two"]["points"] - int(player_current_input) > 0:
                game_state["player_two"]["points"] -= int(res_num)
                game_state["player_two"]["current_input"] = player_current_input
                game_state["player_two"]["EnteredNumber"] = True
                checkWinner(game_state)
            else:
                game_state["player_two"]["current_input"] = game_state["player_two"]["points"]
                game_state["player_two"]["points"] = 0
                game_state["player_two"]["EnteredNumber"] = True
                game_state["player_two"]["GameIsOn"] = False
                checkWinner(game_state)
    else:
        print("error")

def checkWinner(game_state):

    if game_state["player_one"]["EnteredNumber"] == True and game_state["player_two"]["EnteredNumber"] == True:
        current_input_p1 = game_state["player_one"]["current_input"]
        current_input_p2 = game_state["player_two"]["current_input"]
        if int(current_input_p1) > int(current_input_p2):
            print("wins p1 +1")
            game_state["player_one"]["wins"] += 1

        elif int(current_input_p2) > int(current_input_p1):
            print("wins p2 +1")
            game_state["player_two"]["wins"] += 1

        if game_state["player_one"]["wins"] == 5:
            print("one has won")
            game_state["player_one"]["HasWon"] = True;

        if game_state["player_two"]["wins"] == 5:
            print("two has won")
            game_state["player_two"]["HasWon"] = True;

    saveGameState(game_state)
