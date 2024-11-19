values = list(map(int, input().split()))
bottles = values[0] + values[1]
count = 0
while bottles >= values[2]:
    aux = bottles // values[2]
    count += aux
    bottles = bottles % values[2] + aux
    
print(count)