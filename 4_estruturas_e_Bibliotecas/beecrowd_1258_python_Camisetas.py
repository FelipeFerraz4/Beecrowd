from sys import stdin

count = 0
while True:
    number_test = int(stdin.readline().strip())
    if number_test == 0:
        break

    if count > 0:
        print() 

    student = []
    for _ in range(number_test):
        name = stdin.readline().strip()
        data = stdin.readline().split()
        student.append([data[0], data[1], name])

    size_order = {'P': 1, 'M': 2, 'G': 3}
    student = sorted(student, key=lambda x: (x[0], size_order[x[1]], x[2]))

    for item in student:
        print(f'{item[0]} {item[1]} {item[2]}')

    count += 1
