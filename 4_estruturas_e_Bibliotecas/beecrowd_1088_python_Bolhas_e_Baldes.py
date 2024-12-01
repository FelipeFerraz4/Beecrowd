# Uso do Fenwick Tree (ou Binary Indexed Tree - BIT)
from sys import stdin, stdout

def count_inversions(array, n):
    ranks = {value: idx + 1 for idx, value in enumerate(sorted(array))}
    
    fenwick = [0] * (n + 1)
    
    def update(index, value):
        while index <= n:
            fenwick[index] += value
            index += index & -index
    
    def query(index):
        total = 0
        while index > 0:
            total += fenwick[index]
            index -= index & -index
        return total

    inversions = 0
    for i in range(n - 1, -1, -1):
        inversions += query(ranks[array[i]] - 1)
        update(ranks[array[i]], 1)
    
    return inversions

while True:
    line = stdin.readline().strip()
    if line == "0":
        break
    data = list(map(int, line.split()))
    n = data[0]
    array = data[1:]
    
    inversions = count_inversions(array, n)
    if inversions % 2 == 0:
        stdout.write("Carlos\n")
    else:
        stdout.write("Marcelo\n")
