numbers_test = int(input())
for i in range(numbers_test):
    people_numbers = int(input())
    english = False
    previous_language = ''
    for item in range(people_numbers):
        language = input()
        if item == 0:
            previous_language = language
        
        if language != previous_language:
            english = True
    if english:
        print('ingles')
    else:
        print(previous_language)