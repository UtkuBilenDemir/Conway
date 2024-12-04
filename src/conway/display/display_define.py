import pygame
import numpy as np
from alive.neighborhood import alive_neighbors

pygame.init()

# Helper function to draw text
def draw_text(screen, text, color, position, font=pygame.font.Font(None, 36)):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)


# Display the opening menu
def show_menu(screen, screen_size, colors):
    menu_running = True
    while menu_running:
        screen.fill(colors["WHITE"])
        draw_text(screen, "Conway's Game of Life", colors["BLUE"], (screen_size // 2, 50))
        draw_text(screen, "Press M for Manual Setup", colors["BLACK"], (screen_size // 2, 150))
        draw_text(screen, "Press R for Random Initialization", colors["BLACK"], (screen_size // 2, 200))
        draw_text(screen, "Press C to Clear the Grid", colors["BLACK"], (screen_size // 2, 250))
        draw_text(screen, "Press Enter to Start Simulation", colors["BLACK"], (screen_size // 2, 300))
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:  # Manual Setup
                    return "manual"
                elif event.key == pygame.K_r:  # Random Initialization
                    return "random"
                elif event.key == pygame.K_c:  # Clear Grid
                    return "clear"
                elif event.key == pygame.K_RETURN:  # Start Simulation
                    return "start"


def draw_grid(surface, grid, cell_size, grid_size, colors):
    for x in range(grid_size):
        for y in range(grid_size):
            rectangle = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if grid[x, y] == 1:
                pygame.draw.rect(surface, colors["BLACK"], rectangle)
            else:
                pygame.draw.rect(surface, colors["WHITE"], rectangle)
            pygame.draw.rect(surface, colors["GRAY"], rectangle, 1)  # Draw grid lines

# Randomize the grid
def randomize_grid(grid_size):
    return np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.8, 0.2])



def next_generation(grid, grid_size):
    new_grid = np.zeros_like(grid)
    for x in range(grid_size):
        for y in range(grid_size):
            # Count alive neighbors
            alive_sum = alive_neighbors([x, y], grid, grid_size)
            """Conway's Rules"""
            # 1. Underpopulation: Any live cell with fewer than 2 neighbors dies
            # No action needed since the new_grid is zeroes

            # 2. Any live cell with 2 or 3 live neighbors lives
            if grid[x, y] == 1 and alive_sum in [2, 3]:
                new_grid[x, y] = 1

            # 3. Overpopulation: Any live cell with more than 3 live neighbors dies
            # No action needed since the new_grid is zeroes

            # 4.Reproduction: Any dead cell with exactly 3 live neighbors becomes a live cell
            if grid[x, y] == 0 and alive_sum == 3:
                new_grid[x, y] = 1
    return new_grid
