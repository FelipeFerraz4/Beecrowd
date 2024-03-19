value = int(input())
status = 0
number = 0

while status != 1:
    number = int(input())
    if number > value:
        status = 1
        break

numbers = 1
maior = value
while maior <= number:
    maior += value+numbers
    numbers += 1
print(numbers)
