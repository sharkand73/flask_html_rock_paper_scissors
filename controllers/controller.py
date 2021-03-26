from my_app import server
from flask import request, render_template, redirect
from models.rock_paper_scissors import *
from models.player import Player
from models.game_round import GameRound

@server.route('/')
def index():
    return ('Please select your path in the address bar, e.g. /rock/paper')

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









