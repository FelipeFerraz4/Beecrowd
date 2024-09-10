number_test = int(input())

for i in range(number_test):
    word1 = input()
    word2 = input()
    word_test = input()
    
    verificate = 'N'
    
    modifer_word1 = ''
    modifer_word2 = ''
    
    
    for j in range(len(word_test)):
        if word_test[j] == '_':
            modifer_word1 += word1[j]
            modifer_word2 += word2[j]
            
    for j in range(len(modifer_word1)):
        if modifer_word1[j] != modifer_word2[j]:
            if modifer_word1[j] in modifer_word2:
                verificate = 'Y'
            
            if modifer_word2[j] in modifer_word1:
                verificate = 'Y'
    
    print(verificate)
            
            