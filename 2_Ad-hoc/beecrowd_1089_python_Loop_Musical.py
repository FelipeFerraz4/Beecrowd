import sys

while True:
    number_test = int(sys.stdin.readline())
    if number_test == 0:
        break
    notes = list(map(int, sys.stdin.readline().split()))
    notes.insert(0, notes[-1])
    notes.append(notes[1])
    count = 0
    for i in range(1, number_test + 1):
        if notes[i - 1] < notes[i] and notes[i] > notes[i + 1]:
            count += 1
    print(count * 2)            
    