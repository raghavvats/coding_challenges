# **Basic Calculator Project**
## Usage
Input your expression in single quotes, making sure it only includes supported operators and proper order of operations.  
For example:  
    calculator.py '1 + 2'  
    calculator.py '63 * 24 - 34'  

## Support
Tokens are how the expression is parsed and separated to be interpreted mathematically. Support for tokens is limited, so expression complexity is also limited.      

**Supported tokens:**  
    Basic operators: + - * /  
    Parentheses: ( )  
    Numbers: 1 2 3 4 5 6 7 8 9  
    
**Unsupported Tokens:**  
    Functions: ex. sin() cos() tan()  
    Decimals: ex. 1.2  
    Multiple Expressions: ex. '1 + 2, 3 * 4'  
    Other operators: ex. //    

## Implementation
