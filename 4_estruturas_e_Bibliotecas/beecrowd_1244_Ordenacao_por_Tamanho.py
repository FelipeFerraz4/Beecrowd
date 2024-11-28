from sys import stdin

number_test = int(stdin.readline())

for _ in range(number_test):
    text = stdin.readline().strip().split()
    messages = [[len(message), message] for message in text]
    messages.sort(key=lambda x: x[0], reverse=True)
    print(" ".join([item[1] for item in messages]))
