from collections import deque
import heapq


def bfs(maze, start, goal):
    
    queue = deque([start])
    visited = {start}
    parent = {start:None}
    visited_order = []

    path = []

    while queue:
        # Removes the first node from the queue.
        current = queue.popleft()
        visited_order.append(current)

        # Stop searching when the goal is reached and reconstruct the path.
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            break
        row, col = current


         # Check the four possible movement directions.
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1) ]:
            neighbor = (row +dr, col +dc)

            r, c = neighbor

            # Check that the neighbor is inside the maze, passable, and unvisited.
            if(0 <= r < len(maze) and 0 <= c < len(maze[0]) and str(maze[r] [c]) 
                                in ("0","S","G") and neighbor not in visited):
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    # Calculate the path statistics, or use zero if no path was found.
    if path:
        path_length = len(path)
        path_cost = path_length
    else:
        path_length = 0
        path_cost = 0

    # Store the search results for the visualizer.
    stats = {
        "nodes_expanded": len(visited_order),
        "path_length": path_length,
        "path_cost": path_cost
    }
    return path, visited_order, stats



def dfs(maze, start, goal):
    # A stack makes DFS explore the most recently added node first.
    stack = [start]
    visited = {start}
    parent = {start: None}
    visited_order = []
    path = []

    while stack:
        # Removes the top node from the stack.
        current = stack.pop()
        visited_order.append(current)

        # Reconstruct the path when the goal is reached.
        if current == goal:
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            break
        row, col = current

         # Check the four possible movement directions.
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (row + dr, col + dc)
            r, c = neighbor

            # Ignore positions outside the maze, walls, and visited nodes.
            if(0 <= r < len(maze) and 0 <= c < len(maze[0]) and str(maze[r][c])
               in ("0", "S", "G") and neighbor not in visited):
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)
    if path:
        # Calculate the path statistics, or use zero if no path was found.
        path_length = len(path)
        path_cost = path_length
    else:
        path_length = 0
        path_cost = 0

    # Store the search results for the visualizer.
    stats = {
        "nodes_expanded": len(visited_order),
        "path_length": path_length,
        "path_cost": path_cost
    }
    return path, visited_order, stats

    # heuristic function Estimating the remaining distance to the goal.
def manhattan_distance(position, goal):
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


def astar(maze, start, goal, heuristic=manhattan_distance):
    # The priority queue stores (estimated total cost, cost so far, position).
    frontier = [(heuristic(start,goal), 0, start)]
    visited = set()
    parent = {start:None}

    # g_cost records the lowest known cost from the start to each node.
    g_cost = {start:0}
    visited_order = []
    path = []

    # Organize the frontier as a priority queue.
    heapq.heapify(frontier)
    

    while frontier:
        # Select the node with the lowest estimated total path cost.
        f_cost, current_g, current = heapq.heappop(frontier)

        # Skip nodes that have already been expanded.
        if current in visited:
            continue
        
        visited.add(current)
        visited_order.append(current)

        # Reconstruct the path once the goal is reached.
        if current == goal:
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            break

        row, col = current

        # Check the four possible movement directions.
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (row + dr, col + dc)
            r, c = neighbor

            # Only consider positions inside the maze that are passable and unvisited.
            if(0 <= r < len(maze) and 0 <= c < len(maze[0]) and str(maze[r][c])
               in ("0", "S", "G") and neighbor not in visited):

                # Calculate the cost of reaching the neighbor through the current node.
                tentative_g = current_g + 1

                 # Update the neighbor if this route is its first or a cheaper route.
                if neighbor not in g_cost or tentative_g < g_cost[neighbor]:

                    g_cost[neighbor] = tentative_g
                    parent[neighbor] = current

                    # f(n) = g(n) + h(n): cost so far plus estimated remaining cost.
                    f_cost = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(frontier, (f_cost, tentative_g, neighbor))

    # Calculate the path statistics, or use zero if no path was found.
    if path:
        path_length = len(path)
        path_cost = path_length
    else:
        path_length = 0
        path_cost = 0

    # Record the number of expanded nodes, path length, and path cost.
    stats = {
        "nodes_expanded": len(visited_order),
        "path_length": path_length,
        "path_cost": path_cost - 1
    }

    return path, visited_order, stats

#The benchmark maze: 1 represents a wall, 0 an open cell, S the start, and G the goal.
maze = [
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "S", "0", "1", "0", "0", "1", "0", "0", "1"],
    ["1", "0", "0", "0", "1", "0", "1", "1", "0", "1"],
    ["1", "1", "1", "0", "0", "1", "0", "0", "0", "1"],
    ["1", "0", "1", "0", "0", "0", "0", "0", "0", "1"],
    ["1", "0", "0", "0", "0", "0", "1", "1", "0", "1"],
    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
    ["1", "1", "1", "0", "0", "0", "0", "1", "0", "1"],
    ["1", "0", "0", "1", "0", "0", "0", "0", "G", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
]
# Define the starting and goal coordinates as (row, column).
start = (1, 1)
goal = (8, 8)



