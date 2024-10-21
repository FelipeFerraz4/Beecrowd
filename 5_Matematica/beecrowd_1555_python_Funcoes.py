def rafa_function(number1, number2):
    return ((3 * number1)**2) + (number2**2)

def beto_function(number1, number2):
    return (2*(number1**2)) + ((5*number2)**2)

def carlos_function(number1, number2):
    return (-100 * number1) + (number2**3)

number_times = int(input())

for item in range(number_times):
    numbers = list(map(int, input().split()))
    
    if rafa_function(numbers[0], numbers[1]) > beto_function(numbers[0], numbers[1]) and rafa_function(numbers[0], numbers[1]) > carlos_function(numbers[0], numbers[1]):
        print("Rafael ganhou")
    elif beto_function(numbers[0], numbers[1]) > rafa_function(numbers[0], numbers[1]) and beto_function(numbers[0], numbers[1]) > carlos_function(numbers[0], numbers[1]):
        print("Beto ganhou")
    else:
        print("Carlos ganhou")