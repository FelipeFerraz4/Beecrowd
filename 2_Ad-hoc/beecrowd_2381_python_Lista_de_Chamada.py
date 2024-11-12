values = list(map(int, input().split()))
classroom = []
for i in range(values[0]):
    classroom.append(input())
classroom.sort()
print(classroom[values[1] - 1])