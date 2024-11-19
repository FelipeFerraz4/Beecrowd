values = list(map(float, input().split()))
result = 100
result = (result * (100 + values[0])) /100
result = (result * (100 + values[1])) /100
print(f'{result-100:.6f}')
