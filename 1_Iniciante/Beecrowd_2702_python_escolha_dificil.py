meals = input().split()
orders = input().split()
peopleNotSafe = 0
for i in range(3):
    if int(orders[i]) - int(meals[i]) > 0:
        peopleNotSafe += int(orders[i]) - int(meals[i])
print(peopleNotSafe)