tests = int(input())

for i in range(tests):
    values = input().split()
    
    bottles = int(values[0]) // int(values[1])
    bottles = int(values[0]) - (int(values[1]) * bottles) + bottles
    
    print(bottles)