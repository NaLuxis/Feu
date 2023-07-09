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


### Operation ###

def addition(a: int, b: int) -> int:
    return a + b


def substraction(a: int, b: int) -> int:
    return a - b


def division(a: int, b: int) -> int | float:
    return a / b


def multiplication(a: int, b: int) -> int:
    return a * b


def modulo(a: int, b: int) -> int:
    return a % b


### Error ###

def incorect_argument_count(target: List[str], operator: str, number_comparaison: int) -> None:

    match operator:
        case "!=":
            if len(target) != number_comparaison:
                print("Error. Incorect argument count")
                exit()

        case "<=":
            if len(target) <= number_comparaison:
                print("Error. Incorect argument count")
                exit()

        case ">=":
            if len(target) >= number_comparaison:
                print("Error. Incorect argument count")
                exit()

        case "==":
            if len(target) == number_comparaison:
                print("Error. Incorect argument count")
                exit()
        
        case "<":
            if len(target) < number_comparaison:
                print("Error. Incorect argument count")
                exit()

        case ">":
            if len(target) > number_comparaison:
                print("Error. Incorect argument count")
                exit()
