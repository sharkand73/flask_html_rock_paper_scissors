# flask_html_rock_paper_scissors

One of my favourite tasks on the CodeClan Professional Software Development course was this Rock-Paper-Scissors app. 
It allowed me to get creative with the brief, and so I added retro styling (à la 1970s arcade game) as well as an 8-bit rendition of ABBA's "The Winner Takes It All" at the end of the tournament.

# Index
* Setup
* What is it?
* The brief
* Planning

# Setup
You will need to have Flask installed.

1. From the flask_html_rock_paper_scissors directory, type:

      flask run
      
   This starts the server.
      
2. Open a browser window with the address 

      #http://localhost:5000/ 

  and follow the on-screen playing instructions.


# What is it?
This app was the result of a weekend homeowrk project to give us practice in Python, Django, Flask and in particular, practice in server routes / REST.  The game follows 
the well-known game of "rock-paper-scissors" (a.k.a. "paper-scissors-stone") and the user can choose a one-player (playing against the computer) or two-player verison.

In the two-player version, player 1 should cover their corner of the screen so that their opponent cannot see their choice.

A score is kept in the game and the users are free to stop the game when they like, at which point the winner is announced.


# The brief
The brief was to create an app allows the user to play one round of Rock-Paper-Scissors, and that used server routes e.g. /ROCK/PAPER to determine the winner.  
The extension was to make a one-player versiom of the game.  The app was also extended to keep a score tally over several rounds. 

The tech stack is:
* Python 
* Django
* HTML
* CSS

Garage Band along with the "Magical 8bit" plugin and a midi-keyboard were used to create the ABBA jingle at the end.

# Planning
A sketch of the game screen was drawn, and a map of the RESTful routes made.  I also invented a neat mathematical method for determining the winning choice which uses subtraction modulo 3.
This avoided lots of unnecessary if-else statements.

# END
