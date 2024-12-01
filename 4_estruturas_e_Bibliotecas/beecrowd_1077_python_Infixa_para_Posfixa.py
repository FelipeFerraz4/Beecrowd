from sys import stdin

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def associativity(op):
    if op == '^':
        return 'right'
    return 'left'

def infixa_to_posfixa(expression):
    stack = []
    result = []
    
    for char in expression:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while (stack and stack[-1] != '(' and
                   (precedence(stack[-1]) > precedence(char) or
                   (precedence(stack[-1]) == precedence(char) and 
                    associativity(char) == 'left'))):
                result.append(stack.pop())
            stack.append(char)
    while stack:
        result.append(stack.pop())
    return ''.join(result)

number_test = int(stdin.readline())
for _ in range(number_test):
    expression = str(stdin.readline().strip())
    print(infixa_to_posfixa(expression))
    