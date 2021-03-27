from my_app import server
from flask import request, render_template, redirect
from models.rock_paper_scissors import *
from models.player import Player
from models.game_round import GameRound
from models.functions import *

@server.route('/')
def index():
    return render_template('index.html', title="home")

@server.route('/play', methods=['post'])
def play():
    name_1 = request.form["player_1"]
    name_2 = request.form["player_2"]
    if check_names(name_1, name_2) == None:
        return redirect('/')
    player_1 = Player(check_names(name_1, name_2)[0])
    player_2 = Player(check_names(name_1, name_2)[1])
    global current_round 
    current_round = GameRound(player_1, player_2)
    return render_template('play.html', title = "play", current_round=current_round)

@server.route('/route', methods=['post'])
def route():
    choice_1 = request.form["choice_1"]
    choice_2 = request.form["choice_2"]
    return redirect(f'/{choice_1}/{choice_2}')

@server.route('/<choice_1>/<choice_2>')
def outcome(choice_1, choice_2):
    current_round.player_1.assign_choice(choice_1)
    current_round.player_2.assign_choice(choice_2)
    winner = current_round.winner()
    loser = None
    if winner != None:
        loser = current_round.loser()
    return render_template('result.html', winner = winner, loser = loser, title = "Result")
   