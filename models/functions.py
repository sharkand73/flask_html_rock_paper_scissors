def check_names(name_1, name_2):
    if name_1 == "":
        name_1 = "Player1"
    if name_2 == "":
        name_2 = "Player2"
    if name_1 == name_2:
        return None
    else:
        return [name_1.upper(), name_2.upper()]

# def result_string(result):
#     if result == None:
#         return("You chose the same thing!", "Draw!")
#     elif result == current_round.player_1:
#         string_1 = f'<span id={current_round.player_1.choice}>{current_round.player_1.choice}</span> defeats <span id={current_round.player_2.choice}>{current_round.player_2.choice}<span><br>.'
#         string_2 = f'<span id=player-1>{current_round.player_1.name}</span> wins!'
#     else:
#         string_1 = f'<span id={current_round.player_2.choice}>{current_round.player_2.choice}</span> defeats <span id={current.round.player_1.choice}>{current_round.player_1.choice}<span><br>.'
#         string_2 = f'<span id=player-1>{current_round.player_2.name}</span> wins!'
#         return(string_1, string_2)

# def result_title(result):
#     if result == None: 
#         return("Draw")
#     else:
#         return(f'{current_round.winner().name} wins!')
