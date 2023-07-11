############### File tools ###############

from typing import List

### Bool ###

def is_number(target: any) -> bool:

    if str(target).lstrip("+-/*%").isdigit():
        return True
    else:
        return False
    

def is_string(target: any) -> bool:

    if type(target) == str:
        return True
    else:
        return False
    

def is_list(target: any) -> bool:

    if type(target) == list:
        return True
    else:
        return False


def is_empty(target: str | list) -> bool:

    if not target[0]:
        return True
    else:
        return False


def is_equal(target: int, number_comparaison: int) -> bool:

    if target == number_comparaison:
        return True
    else: 
        return False


### Operation ###

def operation(number_a: int, operator: str, number_b: int) -> int | float:
    
    operate = {
        "+" : lambda: number_a + number_b,
        "-" : lambda: number_a - number_b,
        "*" : lambda: number_a * number_b,
        "/" : lambda: number_a / number_b,
        "%" : lambda: number_a % number_b,
    }

    if operator in operate:
        return operate[operator]()
    else:
        raise ValueError(f"Operator {operator} not recognized")


### Error ###

def incorrect_argument_count(target: List[str], operator: str, number_comparison: int) -> None:

    conditions = {
        "!=": lambda: len(target) != number_comparison,
        "<=": lambda: len(target) <= number_comparison,
        ">=": lambda: len(target) >= number_comparison,
        "==": lambda: len(target) == number_comparison,
        "<": lambda: len(target) < number_comparison,
        ">": lambda: len(target) > number_comparison,
    }

    if operator in conditions and conditions[operator]():
        print("Error. Incorrect argument count")
        exit()
    elif operator not in conditions:
        print("Error. Operator not recognized")
        exit()
