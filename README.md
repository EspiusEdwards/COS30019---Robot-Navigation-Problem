# COS30019 - Robot Navigation Problem

## Introduction
This repository contains a Python application that focuses on solving the Robot Navigation problem using various search algorithms. The Robot Navigation problem involves finding the optimal path for a robot in an NxM grid with obstacles, from its starting position to one or more predetermined goals. The application also includes a Graphical User Interface (GUI) to visualize the robot's path-finding progress in real-time.

## Problem Description
The grid in the Robot Navigation problem consists of blank cells and walls that block the robot's movement. Each move has a uniform cost of one. The grid can be represented as a uniform value graph, where the robot needs to find the optimal path from the start to the goal(s).

## Search Algorithms
The application implements six distinct search algorithms:
1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. Greedy Best-First Search (GBFS)
4. A* Search (A*)
5. Bidirectional Search
6. Bidirectional A* Search

Each algorithm has different properties and is efficient in various scenarios. The algorithms are explained in detail in the code and report, including their time complexity, space complexity, and behavior.

## Graphical User Interface (GUI)
The GUI is developed using the Pygame library. It visually represents the grid, with colors indicating different cell types (start, goal, wall, visited, path, etc.). This interface enables users to understand how each algorithm operates and traces its steps.

## Features
- GUI for visualizing the progress of the search algorithms.
- Six search algorithms implemented.
- Command-line operation for specifying the input file and search method.
- Custom stopping condition for Bidirectional A*.

## Known Issues
- For the Bidirectional algorithm, the path found is not always the shortest.
- GUI doesn’t support visualization of large grid dimensions.
- Error handling for input is missing.

## Dependencies
- Python 3.x
- Pygame library

## How to Run

### Command Line Interface

The application is executed through the Disk Operating System (DOS) command-line interface within the Windows Operating System.
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the cloned directory: `cd <repository-directory>`
3. Run the program: `search <input-file> <search-method>`
Replace `<input-file>` with the path to your grid file and `<search-method>` with one of the following options (case-insensitive): bfs, dfs, gbfs, astar, cus1, and cus2 
Output: The number of nodes in the search tree and the pathfinding of the algorithm. In case no solution is found, a message will be displayed indicating that no solution was found.

### Graphical User Interface (GUI)

The graphical user interface (GUI) is designed to be user-friendly, allowing for easy input of data. The screen is divided into two sections:

- **Left Side**: A visual representation of the maze in the form of a grid with cells. The start cell is marked in red, goals are filled in green, and walls are in black. To track progress, visited nodes are shown in light blue, queued nodes in light green, and the pathfinding of the algorithm is marked in yellow.

- **Right Side**: Six buttons for selecting different search algorithms (BFS, DFS, GBFS, A*, cus1, cus2). Only one algorithm can run at a time. To visualize data for a different algorithm, the map needs to be reset using the “Reset” button.

After running the application, you can use the GUI to select the search algorithm and visualize the algorithm in action on the maze.

## Acknowledgments
- The lecture and tutorial materials of the Introduction to AI unit have been crucial in the development of this application.
- The book “Artificial Intelligence: A Modern Approach” 3rd edition by Stuart Russell and Peter Norvig.
