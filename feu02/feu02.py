############### Trouver une forme ###############

import sys

from typing import List
from utile import incorrect_argument_count

### Function ###

def create_board_coords():
    ...


def create_shape_coords():
    ...


def is_equal_char(board, shape) -> List[int]:
    ...


def draw_shape(board_char_coords: List[int]):
    ...


def display_result():
    ...


def handle_error() -> None:

    incorrect_argument_count(sys.argv, ">=", 3)

    for element in sys.argv[1:]:
        ... # regex pour savoir si tout mes arguments sont bien des fichier .txt ( \.(txt?)$ ) 

### Error ###

handle_error()

### Parsing ###

file_name = sys.argv[1]

### Problem solving ###



### Result ###

print()