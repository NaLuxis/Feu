############### Évaluer une expression ###############

import sys
import re

from utile import operation, incorrect_argument_count
from typing import List

### Function ###


def expression_rpn(expression: str) -> List[str]:
    stack_operator = []
    output = []

    tokens = re.findall(r"(\d*\.\d+|\d+|[\+\-\*/%]|[()])", expression)

    for token in tokens:
        if re.match(r"(\d*\.\d+|\d+)", token):
            output.append(token)
        elif re.match(r"[\+\-\*/%]", token):
            while stack_operator and operator_priority(token) <= operator_priority(
                stack_operator[-1]
            ):
                output.append(stack_operator.pop())
            stack_operator.append(token)
        elif token == "(":
            stack_operator.append(token)
        elif token == ")":
            while stack_operator and stack_operator[-1] != "(":
                output.append(stack_operator.pop())
            stack_operator.pop()

    while stack_operator:
        output.append(stack_operator.pop())

    return output


def operator_priority(operator: str) -> int:
    priority = {
        "%": 2,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1,
        "(": 0,
        ")": 0,
    }

    if operator in priority:
        return priority.get(operator, -1)


def evaluate_expression(expression_rpn: List[str]) -> str:
    stack_number = []

    for token in expression_rpn:
        if re.match(r"(\d*\.\d+|\d+)", token):
            stack_number.append(token)
        elif re.match(r"[\+\-\*/%]", token):
            number_2 = stack_number.pop()
            number_1 = stack_number.pop()

            result = operation(float(number_1), token, float(number_2))
            stack_number.append(result)

        if len(stack_number) == 1:
            final_result = stack_number[0]

    return final_result


### Error ###

incorrect_argument_count(sys.argv, "!=", 2)

### Parsing ###

expression = sys.argv[1]

### Problem solving ###

rpn_result = expression_rpn(expression)

result = evaluate_expression(rpn_result)

### Result ###

print(result)
