from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    "PROJECT_PATH": "Projects/Python/conway/src/conway",
    "CELL_SIZE": 20,  # Size of each cell in pixels
    "GRID_SIZE": 30,  # Grid dimensions (GRID_SIZE x GRID_SIZE)
    "WHITE": "255, 255, 255",
    "BLACK": "0, 0, 0",
    "GRAY": "200, 200, 200",
    "BLUE": "0, 0, 255"
} 

with open("conway.ini", "w") as f:
    config.write(f)