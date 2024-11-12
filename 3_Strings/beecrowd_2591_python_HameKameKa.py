word_default = 'hamekameka'

test_number = int(input())
for _ in range(test_number):
    word = input()
    index_k = word.find('k')
    quantity_a = word[:index_k].count('a') * word[index_k:].count('a')
    string_a = 'a' * quantity_a
    print(f'k{string_a}')