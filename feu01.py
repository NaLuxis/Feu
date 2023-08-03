############### Évaluer une expression ###############

import sys

from typing import List
from utile import incorrect_argument_count, operation, is_string

### Function ###

def clean_space(expression_to_clean: str) -> str:

    expression_to_clean = expression_to_clean.replace("(", "( ")
    expression_to_clean = expression_to_clean.replace(")", " )")
    split_expression = expression_to_clean.split(" ")

    new_list = []

    for element in split_expression:
        new_list.append(element)
    
    return new_list


def calcul_operation_priority(elements_list: List[str]) -> str:

    priority_operator = ("*", "/", "%")
    non_priority_operator = ("+", "-")
    
    index = 0
    while index < len(elements_list):
        if elements_list[index] in priority_operator:
            res = operation(float(elements_list[index - 1]), elements_list[index], float(elements_list[index + 1]))
            elements_list[index - 1:index + 2] = [str(res)]
        else:
            index += 1

    index = 0
    while index < len(elements_list):
        if elements_list[index] in non_priority_operator:
            res = operation(float(elements_list[index - 1]), elements_list[index], float(elements_list[index + 1]))
            elements_list[index - 1:index + 2] = [str(res)]
        else:
            index += 1

    return elements_list[0]


def calculate_arithmetic_expression(expression_clean: List[str]) -> str:
    
    stack = [[]]

    for element in expression_clean:
        if element == "(":
            stack.append([])
        elif element == ")":
            sub_expr = stack.pop()
            sub_result = calcul_operation_priority(sub_expr)
            stack[-1].append(sub_result)
        else:
            stack[-1].append(element)
  
    return calcul_operation_priority(stack[0]) 


def handle_error() -> None:

    incorrect_argument_count(sys.argv, "!=", 2)

    if not is_string(sys.argv[1]):
        print("Error. Argument must be string")
        exit()


### Error ###

handle_error()

### Parsing ###

expression = sys.argv[1]

### Problem solving ###

expression_without_space = clean_space(expression)

result = calculate_arithmetic_expression(expression_without_space)

### Result ###

print(result)