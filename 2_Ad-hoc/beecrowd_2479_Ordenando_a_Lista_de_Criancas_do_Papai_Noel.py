number_tests = int(input())
positive = 0
negative = 0
kids = []
for _ in range(number_tests):
    kid = input().split()
    if kid[0] == '+':
        positive += 1
    else:
        negative += 1
        
    kids.append(kid[1])

kids.sort()
for kid in kids:
    print(kid)
print(f'Se comportaram: {positive} | Nao se comportaram: {negative}')
