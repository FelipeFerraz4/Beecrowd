from sys import stdin

vowels = {'a', 'e', 'i', 'o', 'u'}
keyword = stdin.readline().strip()  # Remover espaços e quebras de linha
number_word = int(stdin.readline().strip())

for _ in range(number_word):
    message = stdin.readline().strip()
    result = []
    keyword_length = len(keyword)
    keyword_idx = 0

    for word in message.split():
        if word[0] not in vowels:
            encrypted_word = []
            for j, char in enumerate(word):
                key_char = keyword[keyword_idx % keyword_length]
                encrypted_char = chr(((ord(char) - ord('a')) + (ord(key_char) - ord('a'))) % 26 + ord('a'))
                encrypted_word.append(encrypted_char)
                keyword_idx += 1
            result.append(''.join(encrypted_word))
        else:
            result.append(word)
    print(' '.join(result))
