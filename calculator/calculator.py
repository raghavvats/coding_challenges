import sys
import operator
import re

def is_operator(char):
    '''Check if given char is a supported operator'''
    if char in supported_operations.keys():
        return True
    return False

def tokenize(expression):
    '''
    Tokenize a given expression, returning string with seperated tokens
    
    Supported tokens:
        Basic operators: + - * /
        Parentheses: ( )
        Numbers: 1 2 3 4 5 6 7 8 9

    Unsupported Tokens:
        Functions: ex. sin() cos() tan()
        Decimals: ex. 1.2
        Multiple Expressions: ex. '1 + 2, 3 * 4'
        Other operators: ex. //
    '''
    tokenized_exp = re.findall(r"(\b\d*\.?\d+\b|[\(\)\+\*\-\/])", expression)
    return tokenized_exp

def shunting_yard(expression):
    '''Convert human readable input into reverse rolish notation via the shunting yard algorithm'''
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
    '''Evalute an expression in reverse polish notation'''
    output = []
    while expression:
        if is_operator(expression[0]):
            second = output.pop()
            first = output.pop()
            output.append(supported_operations[expression[0]](first, second))
            expression.pop(0)
        else:
            output.append(expression.pop(0))
    return output

supported_operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

# determines order of operations
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

print(evaluate_RPN(shunting_yard(tokenize(expression)))[0])