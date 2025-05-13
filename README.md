# Connect Four AI Agent

An implementation of a Connect Four game with an AI opponent using the Minimax algorithm with alpha-beta pruning.

## Features

- 6x6 game board
- AI opponent using Minimax algorithm
- Alpha-beta pruning for better performance
- Player vs AI gameplay
- Terminal-based interface

## Implementation Details

- Minimax search with depth 4
- Evaluation function considering:
  - Connected pieces (1, 2, or 3 in a row)
  - Blocking opponent's winning moves
  - Multiple winning threats

## How to Play

1. Run the game:
```bash
python main.py
```

2. Choose your moves by entering:
   - Row number (1-6)
   - Column number (1-6)

3. Try to connect four pieces horizontally, vertically, or diagonally before the AI!

## Files

- `main.py`: Game entry point
- `Board.py`: Board representation and game state
- `Game.py`: Game logic and player interaction
- `ConnectFourAgent.py`: AI implementation with Minimax algorithm

## Requirements

- Python 3.6+