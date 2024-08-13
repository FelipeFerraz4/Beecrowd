numbers_pomekon = int(input())
pomekons = []
for i in range(numbers_pomekon):
    pomekon = input()
    if pomekon not in pomekons:
        pomekons.append(pomekon)

print(f'Falta(m) {151-len(pomekons)} pomekon(s).')