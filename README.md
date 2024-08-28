# Craps Game

Welcome to the Craps Game! This is a simple Python-based simulation of the popular dice game Craps. The game follows the traditional rules of Craps, where players roll two dice and win or lose based on the outcome.

## Table of Contents

- [Game Rules](#game-rules)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Game Rules

The rules of Craps are as follows:

1. The player rolls two dice.
2. If the sum of the dice is **7** or **11**, the player wins.
3. If the sum of the dice is **2**, **3**, or **12** (craps), the player loses, and the casino wins.
4. If the sum is **4**, **5**, **6**, **8**, **9**, or **10**, that sum becomes the player's "goal" number.
5. The player continues to roll the dice until they either:
   - Roll the goal number again (in which case they win), or
   - Roll a **7** (in which case they lose).

## Installation

To run the Craps game, you'll need to have Python installed on your system. You can clone this repository and run the game locally.

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/craps-game.git
    cd craps-game
    ```

2. Run the game:

    ```bash
    python craps_game.py
    ```

## How to Play

After running the game, you'll be prompted with a welcome message and the rules. Press `Enter` to start the game.

- The game will automatically roll two dice for you and display the results.
- Follow the on-screen instructions to determine if you win or lose.
- If the game sets a goal number, keep rolling until you either match the goal or roll a 7.

## Project Structure

```plaintext
.
├── main.py
├── craps_functions.py     # Main game script
└── README.md         # This README file
```

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the project.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

