import sys
import os

import pygame
import numpy as np
# from configparser import ConfigParser
import configparser

config = configparser.ConfigParser()
config.read("conway.ini")
def_config = config["DEFAULT"]

# Adjust sytem path to import local modules
import display.display_define
sys.path.insert(0, os.path.expanduser('~/') + def_config["PROJECT_PATH"])

import display
from display.display_define import draw_grid
# from display.display_define import next_generation

CELL_SIZE = int(def_config["CELL_SIZE"])
GRID_SIZE = int(def_config["GRID_SIZE"])
COLORS = {
    "BLACK": tuple(map(int, def_config["BLACK"].split(","))),
    "WHITE": tuple(map(int,def_config["WHITE"].split(","))),
    "GRAY": tuple(map(int,def_config["GRAY"].split(","))),
    "BLUE": tuple(map(int,def_config["BLUE"].split(",")))
}

SCREEN_SIZE = CELL_SIZE * GRID_SIZE

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()


# Initialize the grid
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)


# Main game loop
def main():
    global grid
    mode = display.display_define.show_menu(screen, SCREEN_SIZE, COLORS)

    if mode == "manual":
        grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
    elif mode == "random":
        grid = display.display_define.randomize_grid(GRID_SIZE)
    elif mode == "clear":
        grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

    running = True
    editing = True



    while running:
        screen.fill(COLORS["WHITE"])
        draw_grid(screen, grid, CELL_SIZE, GRID_SIZE, COLORS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Start or stop the game
                    editing = not editing
                elif event.key == pygame.K_c and editing:  # Clear grid
                    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
            elif event.type == pygame.MOUSEBUTTONDOWN and editing:
                x, y = pygame.mouse.get_pos()
                grid[x // CELL_SIZE, y // CELL_SIZE] ^= 1  # Toggle cell state

        if not editing:
            grid = display.display_define.next_generation(grid, GRID_SIZE)
            pygame.time.delay(100)  # Delay for the simulation

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()