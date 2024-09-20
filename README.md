# Sokoban puzzle solver
This Python project solves Sokoban puzzles using map data from text files. Each solution is created by using graph search algorithms, including search functions under heuristic - cost basis. The solution is then displayed using PyGame.

Heuristic definition for this project can be described as follows:
```python
# Each object's location can be depicted using XY axis, as they're in 2D space.
H = sum(abs(box_location.X - target_location.X) + abs(box_location.Y - target_location.Y))
```

## Requirements
This project uses Python with `pygame` library installed for rendering the solution.
```
pip install pygame
```
You can test this project by running `run-example.bat` or run using the syntax defined below.

## Syntax
```
python main.py
    --map [sokoban map directory]
    --method [map solving algorithm (uses A* if undefined)]
```
Example command:
```
python main.py --map maps/maps/sokoban1.txt --method astar
```
This will start searching for solutions and, depending on the complexity of the map, report back the solution, states generated, node statistics, etc. or return a message if the map is impossible to solve. An example output should look like this:
```
> Solution found: ['U', 'R', 'R', 'U', 'U', 'L', 'L', 'D']
> Number of states generated: 119
> Number of expanded nodes: 86
> Number of moves to reach the target state: 8
> Running time to find the solution: 0.002619028091430664 seconds
```
The solution is then displayed using `pygame`'s graphical interface.

## Supported methods
| Search Algorithm | `--method` |
| --- | --- |
| Breadth-first search | `bfs` |
| Depth-first search | `dfs` |
| Depth-limited search | `dfs_limited_depth` |
| A* search | `astar` |
| Uniform-cost search | `ucs` |
| Greedy search | `greedy` |
| IDA* search | `idas` |

## Map structure
Use Space (not TABs) for empty spaces between objects.
+ `#` - Wall
+ `$` - Box
+ `.` - Target (goal)
+ `*` - Box on target
+ `@` - Player
+ `+` - Player on target

An example of a puzzle map can be described below:
<img align="right" width="258" height="200" src="https://github.com/user-attachments/assets/77042182-ba35-437c-970a-349b51948368">
```
########
#      #
# .#   #
#  $   #
#  @   #
########
```

> [!IMPORTANT]
> All example maps are stored in `maps` folder. You can store map file anywhere, in any extension, as long as it is structured properly, and the program can find and read it. The more complex a map is, the more time this program will take to solve the puzzle.
