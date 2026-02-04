# Chess Game

A simple chess game implemented in Python. This project aims to practice object-oriented programming, game logic, and GUI development.  

## Features
- Two-player mode (local)
- Legal move validation for all chess pieces
- Board displayed in terminal or graphical window (if using pygame)
- Basic game rules: check, checkmate, and stalemate detection

## Tech Stack
- Python 3.x
- Optional: pygame (for GUI), colorama (for terminal colors)

## Installation
1. Clone the repo:

git clone https://github.com/your-username/python-chess-game.git

2. Install dependencies:

pip install -r requirements.txt

3. Run the game:

python main.py


## Project Structure

python-chess-game/
├── main.py
├── chess/
├── assets/
└── tests/


## Future Improvements
- Add AI opponent (Minimax algorithm)
- Add drag-and-drop GUI
- Save/load game states

4. Planning Stage / Steps

Step 1: Core Logic (CLI first)

    Create classes for Board and Piece

    Implement pieces: Pawn, Rook, Knight, Bishop, Queen, King

    Implement movement rules for each piece

    Add turn-based system (Player 1 → Player 2)

    Validate moves (cannot move through other pieces unless allowed)

Step 2: Game Rules

    Detect check and checkmate

    Detect stalemate

    Implement basic victory messages

Step 3: Interface

    Start with terminal-based board (ASCII or Unicode chess symbols)

    Optional: switch to pygame GUI later

Step 4: Testing

    Write unit tests for board setup, moves, and check/checkmate detection

Step 5: Future Enhancements

    AI opponent (Minimax or random moves)

    Save/load games

    Undo/redo moves