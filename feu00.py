############### Échauffement ###############

import sys

from utile import is_number, is_equal, incorrect_argument_count

### Function ###

def display_rectangle(z_axis: int, y_axis: int) -> None:

    corner = "o"
    height = ["|"]
    length = "—"
    space = " "

    if z_axis == 1 and y_axis == 1:
        print(corner)
        exit()

    if z_axis == 1:
        print(corner)

        for element in height * (y_axis - 2):
            if not element[-1]:
                print(f"{element}\n")
            else:
                print(element)

        print(corner)
        exit()

    if y_axis == 1:
        print(f"{corner}{length * (z_axis - 2)}{corner}")
        exit()


    if z_axis != 1 or y_axis != 1:
        print(f"{corner}{length * (z_axis - 2)}{corner}")

        for element in height * (y_axis - 2):
            print(f"{element}{space * (z_axis - 2)}{element}")

    print(f"{corner}{length * (z_axis - 2)}{corner}")
    exit()


def handle_error_argument() -> None:

    incorrect_argument_count(sys.argv, "!=", 3)

    if not is_number(sys.argv[1]) or not is_number(sys.argv[2]):
        print("Error. Each argument needs to be an integer")
        exit()

    if is_equal(int(sys.argv[1]), 0) or is_equal(int(sys.argv[2]), 0):
        print("Error. Zero is don't accept")
        exit()


### Error ###

handle_error_argument()

### Parsing ###

z_axis_number = int(sys.argv[1])

y_axis_number = int(sys.argv[2])

### Problem solving ###

rectangle_to_display = display_rectangle(z_axis_number, y_axis_number)

### Result ###

print(rectangle_to_display)