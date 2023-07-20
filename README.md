# Chess-Engine-DSB
## Chess Engine Data Science Breaks
This project presents a simple, yet competent chess engine in Python, built using the chess library for handling game state and legal move generation. The chess engine is compatible with Universal Chess Interface (UCI), a common protocol for chess engines to communicate with user interfaces.

Moreover, it can be used with the Arena Chess GUI, a free Graphical User Interface (GUI) for chess programs. This compatibility allows the user to visually interact with the game and the chess engine, providing an enriched user experience.

The engine employs an alpha-beta pruning algorithm, a notable search algorithm that helps minimize the number of nodes evaluated by the minimax algorithm in a game tree. It stops evaluating a move as soon as it discovers at least one possibility proving the move to be inferior compared to a previously evaluated move.

The engine also integrates a basic evaluation function that calculates the material balance on the board. Each piece (pawn, knight, bishop, rook, queen) is assigned points and the function then yields a score that represents the material difference between white and black. The engine employs this evaluation function to drive its decisions, aiming to maximize the resultant score.

A minor random factor is incorporated into the evaluation function to encourage move diversity. It's important to note, however, that this randomness doesn't necessarily enhance the engine's performance.

The engine is designed to accept commands from standard input. It listens for the following UCI commands within its main loop:

isready: The engine responds with readyok.
position [fen <fenstring> | startpos ] moves <move1> ... <moveN>: Set the board to a certain position and/or apply a sequence of moves.
go: Instructs the engine to calculate and execute a move. The engine then outputs the best move according to its calculations.
It should be noted that the depth of the search tree is capped at 4 for performance considerations.

Requirements
Python 3.x
python-chess library
Usage
To use this chess engine, you need to run the bundled executable file. The engine will then listen for UCI commands. You can also set it up as an engine in the Arena Chess GUI by pointing to the executable file in the engine configuration settings.
