from Board import GenerateBoard
from ConnectFourAgent import Player, Actions, Result, Winner, Terminal, Utility, Minimax
from time import sleep
import random

class Game:
    def __init__(self, size=3):
        self.state = GenerateBoard(size)
        self.current_player = 1  # Player 1 starts first

    def play(self):
        # random roll to determine who goes first: Agent or Player
        # turn-based moves. For AI, use Minimax algorithm to determine the best move.
        # For Player, take input from the user.
        if random.choice([True, False]):
            print("AI goes first!")
            self.state.player_move = "X"
            self.state.player = 1
        else:
            print("Player goes first!")
            self.state.player_move = "O"
            self.state.player = 2
        '''
        after each turn, update player, player_move and board
        if player's turn, ask for input of i and j in terms of Top, Middle, Bottom Row and Left, Middle, Right Column
        if AI's turn, use Minimax algorithm to determine the best move
        continue till game ends
        '''
        while True:
            self.state.print_board()
            if Terminal(self.state):
                print("Game Over!")
                winner_state = Winner(self.state)
                if winner_state is None:
                    print("It's a draw!")
                else:       
                    winner = "AI" if winner_state == "X" else "Player"
                    print(f"{winner} wins!")
                break
            if self.state.player == 1:
                print("AI's turn!")
                sleep(1)
                print("AI is thinking...") 
                action = self.get_ai_move()
                self.state = Result(self.state, action)
                self.state.player = 2
                self.state.player_move = "O"
            else:
                print("Player's turn!")
                action = self.get_player_move()
                self.state = Result(self.state, action)
                self.state.player = 1
                self.state.player_move = "X"
                print("Player has made its move!")
                sleep(1)

    def get_position_input(self, dimension_name, size):
        """Helper function to get and validate position input"""
        while True:
            print(f"\nChoose {dimension_name} (1-{size}):")
            try:
                choice = input(f"Enter {dimension_name} number: ")
                pos = int(choice) - 1
                
                # Validate position is within board boundaries
                if pos < 0 or pos >= size:
                    print(f"Invalid {dimension_name}! Please enter a number between 1 and {size}.")
                    continue
                    
                return pos
            except ValueError:
                print(f"Invalid input! Please enter a number between 1 and {size}.")

            
    def get_player_move(self):
        while True:
            try:
                i = self.get_position_input("row", self.state.size)
                j = self.get_position_input("column", self.state.size)
            
                if (i < 0 or i >= self.state.size) or (j < 0 or j >= self.state.size):
                    print("Invalid move! Please enter row and column within the board size.")
                    continue
                if self.state.board[i][j] is not None:
                    print("Invalid move! Cell already occupied.")
                    continue
                return (i, j)
            except ValueError:
                print("Invalid input! Please enter two integers separated by space.")
            except IndexError:
                print("Invalid input! Please enter valid row and column indices.")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")


    def get_ai_move(self):
        score, best_move = Minimax(self.state)
        return best_move
        




