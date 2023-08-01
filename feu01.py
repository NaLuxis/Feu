############### Évaluer une expression ###############

import sys

from typing import List, Union
from utile import incorrect_argument_count, operation

### Function ###

def clean_space(expression_to_clean: str) -> str:

    expression_to_clean = expression_to_clean.replace("(", "( ")
    expression_to_clean = expression_to_clean.replace(")", " )")
    split_expression = expression_to_clean.split(" ")

    new_list = []

    for element in split_expression:
        new_list.append(element)
    
    return new_list


def calculate_arithmetic_expression(expression_clean: List) -> Union[int, float]:
    
    stack = []

    for element in expression_clean:
        if element == "(":
            stack.append([])

        elif element == ")":
            sub_result = ... # ici le calcul de mom sub stack

            if stack:
                stack[-1].append(sub_result)
            else:
                return sub_result
        
        else:
            if stack:
                stack[-1].append(element)
            

    return stack

### Error ###

incorrect_argument_count(sys.argv, "!=", 2)

### Parsing ###

expression = sys.argv[1]

### Problem solving ###

expression_without_space = clean_space(expression)

result = calculate_arithmetic_expression(expression_without_space)

### Result ###

print(result)