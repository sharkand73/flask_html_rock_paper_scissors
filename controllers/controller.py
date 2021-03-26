from my_app import server
from flask import request, render_template, redirect

@server.route('/')
def index():
    return ('Hello World!')

@server.route('/rock/paper')
def func_1():
    return ('player 2 wins!')

@server.route('/paper/rock')
def func_2():
    return ('player 1 wins!')

@server.route('/paper/scissors')
def func_3():
    return ('player 2 wins!')

@server.route('/scissors/paper')
def func_4():
    return ('player 1 wins!')

@server.route('/scissors/rock')
def func_5():
    return ('player 2 wins!')

@server.route('/rock/scissors')
def func_6():
    return ('player 1 wins!')

# @server.route('/<name_1>/<name_2>')
# def func_7():
#     return ("It's a draw!")





