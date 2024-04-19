import sys
import operator
import re

def is_operator(char):
    if char in supported_operations.keys():
        return True
    return False

def tokenize(expression):
    tokenized_exp = re.findall(r"(\b\d*\.?\d+\b|[\(\)\+\*\-\/])", expression)
    return tokenized_exp
    
    tokenized_exp = []
    while len(expression) > 0:
        if expression[0].isdigit():
            temp = []
            while expression[0].isdigit():
                temp.append(expression.pop(0))
            tokenized_exp += temp
        elif is_operator(expression[0]):
            tokenize += expression[0]
    return tokenized_exp

def shunting_yard(expression):
    operators = []
    RPN_expression = []
    
    while expression:
        if is_operator(expression[0]):
            if not operators:
                operators.append(expression.pop(0))
            elif precedence[operators[-1]] <= precedence[expression[0]]:
                RPN_expression.append(operators.pop())
            else:
                operators.append(expression.pop(0))
        elif expression[0].isdigit():
            RPN_expression.append(expression.pop(0))
    
    while operators:
        RPN_expression.append(operators.pop())

    for i in range(len(RPN_expression)):
        if RPN_expression[i].isdigit():
            RPN_expression[i] = int(RPN_expression[i])

    return RPN_expression

def evaluate_RPN(expression):
    output = []
    while expression:
        print(output, expression)
        if is_operator(expression[0]):
            second = output.pop()
            first = output.pop()
            output.append(supported_operations[expression[0]](first, second))
            expression.pop(0)
        else:
            output.append(expression.pop(0))
    return output


supported_operations = {
    "+": sum,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "//": operator.floordiv
}

precedence = {
    "*": 1,
    "/": 1,
    "//": 1,
    "+": 2,
    "-": 2
}

if len(sys.argv) != 2:
    print("Usage: calculator.py 'expression'")
    sys.exit(1)
expression = sys.argv[1]

print(evaluate_RPN(shunting_yard(tokenize(expression))))


