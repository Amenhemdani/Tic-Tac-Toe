# Project Instructions: Tic-Tac-Toe Game in Python

## Objective:
Create a two-player Tic-Tac-Toe game that runs in the terminal. The game should allow two players to play against each other, take turns, and determine a winner or a draw.

## Key Concepts:
- Object-Oriented Programming (OOP)
- Lists and Nested Lists
- Control Flow (if-else statements, loops)
- Functions and Methods
- Input Handling
- Error Handling

## Instructions:

### 1. Create a Class Named `TicTacToe`:
- The game will be encapsulated within a `TicTacToe` class to manage the game state and its behavior.

### 2. Initialize the Game Board:
- Create a 3x3 board represented by a nested list. Each cell is initialized with a space `" "`.
- Set the `current_player` to "X", indicating that player "X" will start the game.

### 3. Print the Game Board:
- Implement a method `print_board()` that prints the current state of the board in a user-friendly format. It should show the grid with lines separating the cells.

### 4. Switch Between Players:
- Implement a method `switch_player()` that changes the `current_player` from "X" to "O" and vice versa. This method will be called after each valid move to alternate between players.

### 5. Make a Move:
- Implement a method `make_move(row, col)` that takes the row and column as input and places the current player's mark ("X" or "O") on the board if the selected cell is empty.
- If the move is invalid (i.e., the cell is already occupied), display an error message and prompt the player to try again.

### 6. Check for a Winner:
- Implement a method `check_winner()` that checks if the current player has won the game. A player wins if they have three of their marks in a row, column, or diagonal.

### 7. Check for a Draw:
- Implement a method `check_draw()` that checks if the game is a draw. A draw occurs when all cells are filled, and no player has won.

### 8. Play the Game:
- Implement a method `play()` that starts the game loop. It prompts players to enter their moves and checks for a winner or draw after each move.
- The game loop should continue until there is a winner or a draw.

### 9. Run the Game:
- Create an instance of the `TicTacToe` class and call the `play()` method to start the game.
