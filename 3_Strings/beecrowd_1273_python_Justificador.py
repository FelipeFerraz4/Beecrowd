number_test = 0
while True:
    tests_number = int(input())

    if tests_number == 0:
        break
    if number_test != 0:        
        print()

    words_list = []
    for i in range(tests_number):
        word = input()
        words_list.append(word)
    
    size = max(len(word) for word in words_list)
    
    for word in words_list:
        print(' ' * (size - len(word)) + word)
    number_test += 1
