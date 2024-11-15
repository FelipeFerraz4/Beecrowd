number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(f'A = {number_1}, B = {number_2}, C = {number_3}')
print(f'A = {number_1:>10}, B = {number_2:>10}, C = {number_3:>10}')
print(f'A = {str(number_1).zfill(10)}, B = {str(number_2).zfill(10)}, C = {str(number_3).zfill(10)}')
print(f'A = {number_1:<10}, B = {number_2:<10}, C = {number_3:<10}')