from flask import Flask

server = Flask(__name__)

from controllers import controller

if __name__ == "__main__":
    server.run(debug=True)