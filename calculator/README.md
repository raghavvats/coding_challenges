# **Basic Calculator Project**
Find specifications [here](https://codingchallenges.fyi/challenges/challenge-calculator/).
## Usage
Input your expression in single quotes, making sure it only includes supported operators and proper order of operations.  
For example:  
    calculator.py '1 + 2'  
    calculator.py '63 * 24 - 34'  

## Support
Tokens are how the expression is parsed and separated to be interpreted mathematically. Support for tokens is limited, so expression complexity is also limited.      

**Supported tokens:**  
    - Basic operators: + - * /  
    - Parentheses: ( )  
    - Numbers: 1 2 3 4 5 6 7 8 9  
    
**Unsupported Tokens:**  
    - Functions: ex. sin() cos() tan()  
    - Decimals: ex. 1.2  
    - Multiple Expressions: ex. '1 + 2, 3 * 4'  
    - Other operators: ex. //    

## Implementation
1. Tokenize string using regex, separating any supported tokens (see above) into a list.
2. Execute the [shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm#The_algorithm_in_detail), utilizing a stack to convert the tokenized expression into [reverse polish notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation).
3. Evaluate the RPN expression left-to-right, order of operations having been dealt with in the conversion to RPN.
