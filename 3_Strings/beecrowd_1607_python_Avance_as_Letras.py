test_number = int(input())

for i in range(test_number):
    lettes = input().split()
    word1 = list(lettes[0])
    word2 = list(lettes[1])
    
    count = 0
    for j in range(len(word1)):
        while word1[j] != word2[j]:
            letter_number = ord(word1[j]) + 1
            
            if letter_number > ord('z'):
                letter_number = ord('a')
                
            word1[j] = chr(letter_number)
            count += 1
    
    print(count)
