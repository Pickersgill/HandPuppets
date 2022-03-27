from tkinter import PhotoImage
from random import randint

RED = "#AC3931"
DARK_YELLOW = "#E5D352"
BRIGHT_YELLOW = "#D9E76C"
BLUE = "#537D8D"
PURPLE = "#482C3D"

scheme = [
    RED,
    DARK_YELLOW,
    BRIGHT_YELLOW,
    BLUE,
]

BLOCK_LABEL = BLUE

VAR_TAB = BRIGHT_YELLOW
FUNC_TAB = BRIGHT_YELLOW
OBJ_TAB = BRIGHT_YELLOW

ARRAY_BG = RED

WORKSPACE_BORDER = PURPLE

def random():
    return scheme[randint(0,len(scheme)-1)]

# IMAGES
RES_PATH = "./resources/%s"
PLUS_IMG_PATH = RES_PATH % "plus.png"


