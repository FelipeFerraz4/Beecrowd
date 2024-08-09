tests_number = int(input())

for i in range(tests_number):
    words = input().split()
    word1 = words[0]
    word2 = words[1]

    count1 = 0
    count2 = 0

    while count1 < len(word1) or count2 < len(word2):
        if count1 < len(word1):
            print(word1[count1], end='')
            count1 += 1

        if count2 < len(word2):
            print(word2[count2], end='')
            count2 += 1 
    print()
