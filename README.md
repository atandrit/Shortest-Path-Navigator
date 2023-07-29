
# Shortest Path Navigator

The goal of this project is to develop a Python program that uses the A* (A-star) algorithm to find the shortest path between two points on a graph or grid. A* is a widely used pathfinding algorithm that is particularly effective in finding the shortest path in a grid or graph with obstacles.

The program will take a graph or grid with obstacles and two points (start and end) as input, and it will output the shortest path between the two points.

## Documentation


The A* algorithm is a heuristic search algorithm that uses a combination of heuristic (estimated) cost and actual cost to find the shortest path between two points. The algorithm works by exploring the nodes (vertices) in the graph or grid, evaluating each node based on the sum of the actual cost to reach that node and the heuristic cost to reach the goal. The algorithm selects the next node with the lowest evaluation function and repeats the process until the goal is reached.

To use the program, follow these steps:

1. Install the required Python packages (e.g., pygame) using pip or another package manager.
2. Import the A-star algorithm function into your Python program.
3. Define the graph or grid as a matrix, where each element represents a node and the value represents the cost to traverse that node.
4. Define the start and end points on the grid.
5.  the A-star function with the graph or grid, start and end points as input.
6. The A-star function will output the shortest path between the start and end points.
## Output

Landing Window

![Landing Window](https://user-images.githubusercontent.com/91213354/222565028-36892526-d437-492d-b6ad-134101a5160a.png)

After Defining the Initial and Goal Nodes

![Initial and Goal Node](https://user-images.githubusercontent.com/91213354/222564950-21386b74-18bc-4984-aa53-587dd1e3cb5e.png)

After Adding Obstacles

![Obstacles](https://user-images.githubusercontent.com/91213354/222564866-3f8978dc-ba4c-4929-bacd-262a38b04eec.png)

Result

![Result](https://user-images.githubusercontent.com/91213354/222564315-51bc3572-920c-40e3-a58e-5e3456f2703e.png)


## Author

- Atandrit Chatterjee ([@atandrit](https://github.com/atandrit))

