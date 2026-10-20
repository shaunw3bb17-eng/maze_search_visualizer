# Maze Search Algorithm Visualizer

A Python project that implements and visualizes Breadth-First Search (BFS), Depth-First Search (DFS), and A* Search using Pygame.

## Features

- **Breadth-First Search (BFS):** Explores the maze level by level to find a shortest path in an unweighted maze.
- **Depth-First Search (DFS):** Explores one path as far as possible before backtracking.
- **A* Search:** Uses path cost and the Manhattan distance heuristic to guide the search toward the goal.
- **Animated Visualization:** Displays explored cells and highlights the final path.
- **Algorithm Comparison:** Compares the number of nodes expanded and path lengths for all three algorithms.
- **Adjustable Animation Speed:** Use the Up and Down arrow keys to control the visualization speed.

## Technologies Used

- Python 3.13
- Pygame
- Git and GitHub

## Installation

Install Pygame using:

```bash
py -3.13 -m pip install pygame
```

## How to Run

Place `maze_solver.py` and `maze_visualizer.py` in the same directory.

Run the visualizer from the terminal:

```bash
py -3.13 maze_visualizer.py
```

## Controls

- **BFS:** Visualize Breadth-First Search.
- **DFS:** Visualize Depth-First Search.
- **A\*:** Visualize A* Search.
- **Compare:** Show or hide the algorithm comparison statistics.
- **Up Arrow:** Increase animation speed.
- **Down Arrow:** Decrease animation speed.

## Project Structure

```text
maze-search-visualizer/
├── maze_solver.py
├── maze_visualizer.py
└── README.md
```

## Author
Shaun Webb
