test_number = int(input())
for i in range(test_number):
    phaser = input().lower()
    letter_frequnet = {}
    for letter in phaser:
        if 'a' <= letter <= 'z':
            if letter in letter_frequnet:
                letter_frequnet[letter] += 1 
            else:
                letter_frequnet[letter] = 1
    max_frequent = max(letter_frequnet.values())
    letters_max_frequent = [letter for letter, frequent in letter_frequnet.items() if frequent == max_frequent]
    letters_max_frequent.sort()
    print(''.join(letters_max_frequent))