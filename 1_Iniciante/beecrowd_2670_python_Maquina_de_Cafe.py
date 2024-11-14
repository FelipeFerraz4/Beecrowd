ground_floor = int(input())
first_floor = int(input())
second_floor = int(input())

option = []
option.append(2 * first_floor + 4 * second_floor)
option.append(2 * ground_floor + 2 * second_floor)
option.append(4 * ground_floor + 2 * first_floor)
print(min(option))