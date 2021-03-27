from my_app import server
from flask import request, render_template, redirect
from models.rock_paper_scissors import *
from models.player import Player
from models.game_round import GameRound

@server.route('/')
def index():
    return render_template('index.html', title="home")

@server.route('/<choice_1>/<choice_2>')
def outcome(choice_1, choice_2):
    player_1 = Player("Andy")
    player_1.assign_choice(choice_1)
    player_2 = Player("Evelyn")
    player_2.assign_choice(choice_2)
    current_round = GameRound(player_1, player_2)
    if current_round.winner():
        return (f'{current_round.winner().name} wins with {current_round.winner().choice}!')
    else:
        return (f'You both chose {current_round.player_1.choice}.  It is a draw!')

@server.route('/play', methods=['post'])
def start():
    name_1 = request.form["player_1"]
    name_2 = request.form["player_2"]
    if name_1 == "":
        name_1 = "Player1"
    if name_2 == "":
        name_2 = "Player2"
    if name_1 == name_2:
        return redirect('/')
    player_1 = Player(name_1)
    player_2 = Player(name_2)
    return render_template('play.html', title = "play", player_1=player_1, player_2=player_2)