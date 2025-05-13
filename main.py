from Board import GenerateBoard
from ConnectFourAgent import Player, Actions, Result, Winner, Terminal, Utility, Minimax, Evaluate
from Game import Game

game = Game(size=6)  # Initialize the game with a 4x4 board
game.play()