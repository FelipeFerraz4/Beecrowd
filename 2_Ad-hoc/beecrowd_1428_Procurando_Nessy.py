test_number = int(input())
for _ in range(test_number):
    values = list(map(int, input().split()))
    
    print((values[0]//3) * (values[1]//3))