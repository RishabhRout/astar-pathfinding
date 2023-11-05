# A* Pathfinding Algorithm

## Description

This project implements the A* pathfinding algorithm, a popular pathfinding algorithm used in various applications such as robotics, video games, and map navigation. The A* algorithm efficiently finds the shortest path from a starting point to a target point on a grid or map.

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/RishabhRout/astar-pathfinding.git
   ```

2. Navigate to the project directory:

   ```shell
   cd astar-pathfinding
   ```

3. Run the example code to see how the A* algorithm works with a sample map:

   ```shell
   python main.py
   ```

## Assumptions

The original question suggests to use a map with only 0 & 1.
 - 0 is allowed node 
 - 1 is blocked node

## Example Usage

You can use the A* pathfinding algorithm to find a path from a start point to a goal point on a map. Here's how to use it:

```python
from astar import astar

# Define a map with obstacles (use 'x' to represent obstacles)
map = [
    ['0', '1', '2', '1', '0'],
    ['1', '1', '1', '1', '0'],
    ['1', '1', 'x', 'x', 'x'],
    ['0', '1', '1', '1', '0'],
    ['1', '0', '0', '0', '0']
]

# Specify the starting and goal points
start_point = (0, 0)
goal_point = (4, 4)

# Find the path using the A* algorithm
path = astar(start_point, goal_point, map)

# Visualize the path by replacing map cells with '+'
if path:
    for point in path:
        map[point[0]][point[1]] = '+'

# Print the map with the path
print('\n'.join([' '.join([str(cell) for cell in row]) for row in map]))
```

## Goals

- [x] Implement the A* pathfinding algorithm.
- [x] Visualize the path on a map.
- [ ] Add support for custom map input.
- [ ] Allow custom obstacle symbols.
- [ ] Optimize the code for larger maps.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The A* pathfinding algorithm is a classic algorithm widely used in computer science and AI.

Feel free to contribute to this project, report issues, or suggest improvements. Happy pathfinding!
