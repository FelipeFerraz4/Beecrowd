import sys

def paula_math_game(expressions):
    results = []
    for expression in expressions:
        a = int(expression[0])
        b = int(expression[2])
        operator = expression[1]

        if a == b:
            results.append(a * b)
        elif operator.isupper():
            results.append(b - a)
        else:
            results.append(a + b)
    
    return results

# Example usage:
if __name__ == "__main__":
    input = sys.stdin.readline
    number_test = int(input())
    data = []
    for _ in range(number_test):
        data.append(input())
    results = paula_math_game(data)
    for result in results:
        print(result)