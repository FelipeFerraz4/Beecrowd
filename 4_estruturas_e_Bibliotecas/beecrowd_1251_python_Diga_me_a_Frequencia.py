count = 0
while True:
    try:
        text = input()
        chars = {}
        for char in text:
            if ord(char) in chars:
                chars[ord(char)] += 1
            else:
                chars[ord(char)] = 1
        sorted_chars = sorted(chars.items(), key=lambda x: (x[1], -x[0]))
        if count > 0:
            print()
        for char, value in sorted_chars:
            print(f'{char} {value}')
        count += 1
    except EOFError:
        break
