

# 🐍 Advanced Snake Game

This is a classic "Snake" arcade game built from scratch using Python and the Pygame library. Far from a basic tutorial clone, this project features  smart spawning algorithms, dynamic difficulty, and persistent data tracking to create a highly polished gaming experience.

## ✨ Advanced Features & Mechanics (Under the Hood)

This game includes several sophisticated systems to ensure smooth gameplay and a great visual experience:

* 🧠 Smart Food Spawning Algorithm: The food generation system scans the entire grid to create an array of safe coordinates. It mathematically excludes the UI borders and the snake's current body cells, guaranteeing an apple will never spawn inside a wall or the snake itself.
* 🛡️ Anti-Suicide Keystroke Protection: A built-in vector check compares the player's input against the physical location of the snake's "neck". This prevents the snake from instantly snapping its own neck (turning 180 degrees) if the player accidentally presses two opposite keys within the same millisecond.
* 🛑 Fair Game Over System: Upon collision, the game forces Pygame to render the exact final frame of the crash and initiates a 1-second programmatic pause. This gives the player time to visually process exactly where they crashed before transitioning to the Game Over screen.
* 📈 Dynamic Difficulty Scaling: The game engine's internal tick rate (FPS/speed) automatically increases as the snake consumes apples, steadily ramping up the difficulty.
* 💾 Data Persistence (High Score): The game tracks your highest score and saves it to a local file. Your best record persists even if you completely close and restart the application.
* ⏸️ Visual Pause System: Pressing `ESC` freezes the event timer and renders a sleek, semi-transparent overlay to dim the active game board without losing track of your position.

## 🛠 Requirements
* Python 3.x
* Pygame

## 🚀 Installation

Ensure you have Python installed on your system.

Install the required Pygame library by running the following command in your terminal:

```bash
pip install pygame
```

## ▶️ How to Run
After installing the dependencies, navigate to the root folder of the project and run the main script:

```bash
python main.py
```

## 🎮 Controls
The game supports multiple control schemes and an interactive menu:

* Movement:
* Use the Arrow keys (Up, Left, Down, Right) to navigate.
* Alternatively, use the `WASD` keys (`W` for Up, `A` for Left, `S` for Down, `D` for Right).
* Main Menu: Use your Mouse to click the "Press to start the game" button to begin playing.
* Pause & Resume: Press the `ESC` key to pause the game at any time and press it again to resume.
* Game Over Screen:
* `R` — Instantly restart the game.
* `Q` — Quit the application safely.

## 🏆 Rules and Scoring
* Objective: Guide the snake to eat the apples. Each apple grants +10 points.
* Win Condition: If you manage to grow the snake so large that it occupies every single free tile on the grid, the food spawner will detect no free space and automatically trigger a victory/end state!
* Warning: Be careful — colliding with the outer walls or biting your own tail will result in an immediate Game Over.
