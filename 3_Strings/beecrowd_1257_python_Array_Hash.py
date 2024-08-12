tests_numbers = int(input())

for i in range(tests_numbers):
    line_number = int(input())
    words = []
    for j in range(line_number):
        words.append(input())
    hash = 0
    for j in range(len(words)):
        for k in range(len(words[j])):
            hash += (ord(words[j][k]) % 65) + j + k
    print(hash)