word = input()
vowels = []
for letter in word:
    if letter in 'aeiou':
        vowels.append(letter)
half = len(vowels)//2
happy = True
for i in range(half):
    if vowels[i] != vowels[len(vowels) - i - 1]:
        happy = False
if happy:
    print('S')
else:
    print('N')