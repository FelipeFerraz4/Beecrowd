def test_invalid(text):
    if len(text) != 8 or '-' not in text:
        return True
    
    for letter in text[:3]:
        if letter < 'A' or letter > 'Z':
            return True
    for letter in text[4:]:
        if letter < '0' or letter > '9':
            return True
    return False

number = int(input())
for _ in range(number):
    text = input()

    if test_invalid(text):
        print('FAILURE')
    elif text[7] == '1' or text[7] == '2':
        print('MONDAY')
    elif text[7] == '3' or text[7] == '4':
        print('TUESDAY')
    elif text[7] == '5' or text[7] == '6':
        print('WEDNESDAY')
    elif text[7] == '7' or text[7] == '8':
        print('THURSDAY')
    else:
        print('FRIDAY')