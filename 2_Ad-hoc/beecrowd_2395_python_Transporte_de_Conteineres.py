values_container = list(map(int, input().split()))
values_navy = list(map(int, input().split()))

result = (values_navy[0] // values_container[0])
result *= (values_navy[1] // values_container[1])
result *= (values_navy[2] // values_container[2])

print(result)