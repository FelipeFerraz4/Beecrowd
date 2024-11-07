number_tests = int(input())
values = input().split()
phase = ''
for item in values:
    phase += chr(int(item, base=16))

print(phase)