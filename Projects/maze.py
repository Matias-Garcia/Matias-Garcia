# Prerequisite run: pip3 install pygame
# Use keys to move

import pygame
import random

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
GRID_SIZE = 20
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

# Maze dimensions
COLS = SCREEN_WIDTH // GRID_SIZE
ROWS = SCREEN_HEIGHT // GRID_SIZE

# Generate maze using Recursive Backtracking
def generate_maze(cols, rows):
    maze = [[1 for _ in range(cols)] for _ in range(rows)]
    stack = []
    start_x, start_y = 0, 0
    maze[start_y][start_x] = 0
    stack.append((start_x, start_y))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if 0 <= nx < cols and 0 <= ny < rows and maze[ny][nx] == 1:
                maze[y + dy][x + dx] = 0
                maze[ny][nx] = 0
                stack.append((nx, ny))
                break
        else:
            stack.pop()

    return maze

# Draw maze
def draw_maze(maze):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Main game loop
def main():
    maze = generate_maze(COLS, ROWS)
    player_pos = [0, 0]
    goal_pos = [COLS - 1, ROWS - 1]

    running = True
    while running:
        screen.fill(WHITE)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement
        keys = pygame.key.get_pressed()
        x, y = player_pos
        if keys[pygame.K_UP] and y > 0 and maze[y - 1][x] == 0:
            player_pos[1] -= 1
        if keys[pygame.K_DOWN] and y < ROWS - 1 and maze[y + 1][x] == 0:
            player_pos[1] += 1
        if keys[pygame.K_LEFT] and x > 0 and maze[y][x - 1] == 0:
            player_pos[0] -= 1
        if keys[pygame.K_RIGHT] and x < COLS - 1 and maze[y][x + 1] == 0:
            player_pos[0] += 1

        # Check if player reached the goal
        if player_pos == goal_pos:
            print("You Win!")
            running = False

        # Draw maze
        draw_maze(maze)

        # Draw player
        pygame.draw.rect(
            screen, BLUE, 
            (player_pos[0] * GRID_SIZE + 2, player_pos[1] * GRID_SIZE + 2, GRID_SIZE - 4, GRID_SIZE - 4)
        )

        # Draw goal
        pygame.draw.rect(
            screen, RED, 
            (goal_pos[0] * GRID_SIZE + 2, goal_pos[1] * GRID_SIZE + 2, GRID_SIZE - 4, GRID_SIZE - 4)
        )

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
