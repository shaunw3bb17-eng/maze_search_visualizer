import pygame
# Import the search algorithms from maze_solver.py.

from maze_solver import bfs, dfs, astar

# Define the maze used for the visualization.
# 1 represents a wall, 0 represents an open cell,
# S represents the start, and G represents the goal.
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

# Set the starting and goal positions using (row, column).
start = (1, 1)
goal = (8, 8)

# Define the size of each maze cell and calculate the maze dimensions.
CELL_SIZE = 50
ROWS = len(maze)
COL = len(maze[0])

# Define the RGB colours used to draw the maze and its elements.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (220, 0, 0)
GREY = (200, 200, 200)
BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)

BUTTON_COLOR = (210, 210, 210)
SELECTED_BUTTON_COLOR = (100, 180, 255)
BUTTON_TEXT_COLOR = (0, 0, 0)

# Set the dimensions of the algorithm buttons.
BUTTON_WIDTH = 80
BUTTON_HEIGHT = 40

# Create clickable buttons for selecting each algorithm and comparing results.
BFS_BUTTON = pygame.Rect(520, 40, BUTTON_WIDTH, BUTTON_HEIGHT)
DFS_BUTTON = pygame.Rect(610, 40, BUTTON_WIDTH, BUTTON_HEIGHT)
ASTAR_BUTTON = pygame.Rect(700, 40, BUTTON_WIDTH, BUTTON_HEIGHT)
COMPARE_BUTTON = pygame.Rect(520, 260, 120, BUTTON_HEIGHT)

# Set the initial algorithm and hide the comparison panel.
algorithm = "BFS"
show_comparison = False

# Run the currently selected search algorithm.
def run_algorithm():
    if algorithm == "BFS":
        return bfs(maze, start, goal)
    elif algorithm == "DFS":
        return dfs(maze, start, goal)
    elif algorithm == "A*":
        return astar(maze, start, goal)

# Run all three algorithms and collect their statistics for comparison.    
def compare_algorithm():
    bfs_result = bfs(maze, start, goal)
    dfs_result = dfs(maze, start, goal)
    astar_result = astar(maze, start, goal)

    # Return the statistics from each algorithm's result.
    return {
        "BFS": bfs_result[2],
        "DFS": dfs_result[2],
        "A*": astar_result[2]
    }

 # Run the selected algorithm and store its path, visit order, and statistics.   
path, visited_order, stats = run_algorithm()

# Convert the visited positions into a set for efficient membership checks.
visited_set = set(visited_order)

# Calculate the comparison statistics for all three algorithms.
comparison_stats = compare_algorithm()

# Set the initial animation delay and animation progress counters.
animation_delay = 100
visited_index = 0
path_index = 0

# Initialize Pygame and create the font used for displaying text.
pygame.init()

font = pygame.font.SysFont(None, 28)
TEXT_COLOR = (0, 0, 0)


# Set the dimensions of the application window.
WIDTH = 800
HEIGHT = 600

# Create the window and set its title.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Maze Solver Visualization")

# Keep the application running until the user closes the window.
running = True

while running:
    # Check for keyboard and mouse events.
    for event in pygame.event.get():

         # Stop the application when the window is closed.
        if event.type == pygame.QUIT:
            running = False

        # Allow the user to adjust the animation speed with the arrow keys.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:

                # Reduce the delay to make the animation faster.
                animation_delay = max(10, animation_delay - 10)
            elif event.key == pygame.K_DOWN:

                # Increase the delay to make the animation slower.
                animation_delay = min(500, animation_delay + 10)

        # Check whether the user clicked a button.
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Toggle the comparison panel when the Compare button is clicked.
            if COMPARE_BUTTON.collidepoint(event.pos):
                show_comparison = not show_comparison
            else:

                # Determine which algorithm button was selected.
                selected_algorithm = None

                if BFS_BUTTON.collidepoint(event.pos):
                    selected_algorithm = "BFS"
                elif DFS_BUTTON.collidepoint(event.pos):
                    selected_algorithm = "DFS"
                elif ASTAR_BUTTON.collidepoint(event.pos):
                    selected_algorithm = "A*"

                # Run the newly selected algorithm if it differs from the current one.
                if selected_algorithm is not None and selected_algorithm != algorithm:
                    algorithm = selected_algorithm
                    path, visited_order, stats = run_algorithm()
                    visited_set = set(visited_order)
                    visited_index = 0
                    path_index = 0

    # Clear the window before drawing the next frame.
    screen.fill(WHITE)

    # Highlight the button belonging to the currently selected algorithm.
    if algorithm == "BFS":
        bfs_color = SELECTED_BUTTON_COLOR
    else:
        bfs_color = BUTTON_COLOR

    if algorithm == "DFS":
            dfs_color = SELECTED_BUTTON_COLOR
    else:
        dfs_color = BUTTON_COLOR

    if algorithm == "A*":
            astar_color = SELECTED_BUTTON_COLOR
    else:
        astar_color = BUTTON_COLOR

    # Draw the three algorithm buttons.
    pygame.draw.rect(screen, bfs_color, BFS_BUTTON)
    pygame.draw.rect(screen, dfs_color, DFS_BUTTON)
    pygame.draw.rect(screen, astar_color, ASTAR_BUTTON)

    # Highlight the Compare button when the comparison panel is visible.
    if show_comparison:
        compare_color = SELECTED_BUTTON_COLOR
    else:
        compare_color = BUTTON_COLOR

    pygame.draw.rect(screen, compare_color, COMPARE_BUTTON)

    # Create and display the text on the Compare button.
    compare_text = font.render("Compare", True, BUTTON_TEXT_COLOR)
    screen.blit(
        compare_text,
        compare_text.get_rect(center=COMPARE_BUTTON.center)
    )

    # Create the labels for the algorithm buttons.
    bfs_text = font.render("BFS", True, BUTTON_TEXT_COLOR)
    dfs_text = font.render("DFS", True, BUTTON_TEXT_COLOR)
    astar_text = font.render("A*", True, BUTTON_TEXT_COLOR)

    # Position the algorithm labels in the centre of their buttons.
    screen.blit(bfs_text, bfs_text.get_rect(center=BFS_BUTTON.center))
    screen.blit(dfs_text, dfs_text.get_rect(center=DFS_BUTTON.center))
    screen.blit(astar_text, astar_text.get_rect(center=ASTAR_BUTTON.center))


    # Draw each cell in the maze using its current visualization state.
    for row in range(ROWS):
        for col in range(COL):

            # Walls, start, and goal take priority over animation colours.
            if maze[row][col] == "1":
                color = BLACK
            elif maze[row][col] == "S":
                color = RED
            elif maze[row][col] == "G":
                color = GREEN

            # Highlight the discovered final path in yellow.
            elif (row, col) in path[:path_index]:
                color = YELLOW

            # Highlight explored positions in blue as the search progresses.
            elif (row,col) in visited_order[:visited_index]:
                color = BLUE
            else:

                # Keep cells that have not yet been explored white.
                color = WHITE

            # Draw the filled rectangle representing the current cell.
            pygame.draw.rect(
                screen,
                color,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

            # Draw a grey border around the cell.
            pygame.draw.rect(
                screen,
                GREY,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                1
            )


    # Prepare the text showing the animation delay and algorithm statistics.
    speed_text = font.render(
        f"animatioin delay: {animation_delay} ms", True, TEXT_COLOR
    )
    expanded_text = font.render(
        f"Nodes Expanded: {stats['nodes_expanded']}", True, TEXT_COLOR
    )

    path_length_text = font.render(
        f"Path Length: {stats['path_length']}", True, TEXT_COLOR
    )

    # Display the path cost only for A*.
    if algorithm == "A*":
        path_cost_value = stats["path_cost"]
    else:
        path_cost_value = " -"
    path_cost_text = font.render(
        f"Path Cost: {path_cost_value}", True, TEXT_COLOR
    )

     # Display the current animation delay.
    screen.blit(speed_text, (520, 220))

    # Display the comparison panel and statistics when enabled.
    if show_comparison:
        comparison_title = font.render("Algorithm Comparison ", True, TEXT_COLOR)
        screen.blit(comparison_title, (520, 310))

        # Retrieve the statistics for each algorithm.
        bfs_comparison = comparison_stats["BFS"]
        dfs_comparison = comparison_stats["DFS"]
        astar_comparison = comparison_stats["A*"]

         # Format the comparison results for display.
        bfs_stats_text = font.render(
            f"BFS: {bfs_comparison['nodes_expanded']} nodes, path {bfs_comparison['path_length']}",
            True, TEXT_COLOR
        )
        dfs_stats_text = font.render(
            f"DFS: {dfs_comparison['nodes_expanded']} nodes, path {dfs_comparison['path_length']}",
            True, TEXT_COLOR
        )
        astar_stats_text = font.render(
            f"A*: {astar_comparison['nodes_expanded']} nodes, path {astar_comparison['path_length']}",
            True, TEXT_COLOR
        )

        # Draw the comparison statistics below the panel title.
        screen.blit(bfs_stats_text, (520, 350))
        screen.blit(dfs_stats_text, (520, 385))
        screen.blit(astar_stats_text, (520, 420))

    # Show the selected algorithm's statistics after its animation finishes.
    if visited_index >= len(visited_order) and path_index >= len(path):
        screen.blit(expanded_text, (520, 100))
        screen.blit(path_length_text, (520, 140))
        screen.blit(path_cost_text,(520, 180))

     # Update the display so the current frame becomes visible.
    pygame.display.update()

    # Animate the explored positions first, then highlight the final path.
    if visited_index < len(visited_order):
        visited_index += 1
    elif path_index < len(path):
        path_index += 1



    # Pause briefly to control the animation speed.
    pygame.time.delay(animation_delay)

# Close Pygame when the main loop ends.
pygame.quit()