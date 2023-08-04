############### Trouver une forme ###############

import sys

from typing import List, Tuple
from utile import incorrect_argument_count

### Function ###

def read_file(file_name: str) -> List[List[str]]:
    
    my_file = f"text/{file_name}"

    with open(my_file, "r") as f:
        content = f.readlines()

        if not content:
            exit("Erreur. The file is empty.")

        element = []

        for lines in content:
            element.append([lines[:-1]])
        
        return element
    

def create_coords(element: List[List[str]]) -> List[Tuple[List[int],str]]:
    
    coords_and_value_element= []
    first_line = element[0][0]
    space = len(first_line) - len(first_line.lstrip(" "))
    
    for y_axis, line in enumerate(element):
        for x_axis, char in enumerate(line[0]):
            coords_and_value_element.append([[x_axis - space, y_axis], char])

    return coords_and_value_element


def find_equal_shape(shape_file_name: str) -> List[int]:
    
    board_coords_list = create_coords(read_file("board.txt"))
    shape_coords_list = create_coords(read_file(shape_file_name))

    for coords_and_value in shape_coords_list:
        if coords_and_value[0] == [0,0]:
            shape_char = coords_and_value[1]

    for coords_and_value in board_coords_list:
        if coords_and_value[1] == shape_char:
            board_char = coords_and_value[0]

    



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

# readed_file = read_file("board.txt")

# element_with_coords = create_coords(readed_file)

shape_is_equal_or_not = find_equal_shape("to_find.txt")

### Result ###

print(shape_is_equal_or_not)