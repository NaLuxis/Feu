############### Trouver une forme ###############

import sys

from typing import List
from utile import incorrect_argument_count

### Function ###

def read_file(file_name: str) -> List[List[str]]:
    
    my_file = f"/home/yoann/Documents/Feu/text/{file_name}"

    with open(my_file, "r") as f:
        content = f.readlines()

        if not content:
            print("Erreur. The file is empty.")
            exit()

        board = []

        for lines in content:
            board.append([lines[:-1]])
        
        return board
    

def create_coords(element: List[List[str]]) -> List[List[int]]:
    
    coords_board = []
    
    for y_axis, line in enumerate(element):
        for x_axis, char in enumerate(line[0]):
            coords_board.append([x_axis, y_axis])

    return coords_board


def is_equal_char(board, shape) -> List[int]:
    ...


def draw_shape(board_char_coords: List[int]):
    ...


def display_result():
    ...


def handle_error() -> None:

    incorrect_argument_count(sys.argv, "!=", 3)

    for element in sys.argv[1:]:
        ... # regex pour savoir si tout mes arguments sont bien des fichier .txt ( \.(txt?)$ ) 

### Error ###

#handle_error()

### Parsing ###

# file_board = sys.argv[1]

# file_shape = sys.argv[2]

### Problem solving ###

readed_file = read_file("board.txt")

element_with_coords = create_coords(readed_file)

### Result ###

print(element_with_coords)