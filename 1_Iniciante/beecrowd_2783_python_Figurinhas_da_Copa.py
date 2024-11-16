data = list(map(int, input().split()))
stamps = list(map(int, input().split()))
stickers = list(map(int, input().split()))

stamp = len(stamps)
for i in range(stamp):
    if stamps[i] not in stickers:
        stamp -= 1
print(len(stamps) - stamp)
