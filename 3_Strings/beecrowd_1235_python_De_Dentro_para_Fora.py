tests_number = int(input())
for i in range(tests_number):
    text = input()
    size_text = len(text)
    text_origen = []
    for j in range(size_text//2-1, -1, -1):
        text_origen.append(text[j])
    for j in range(size_text-1, size_text//2-1, -1):
        text_origen.append(text[j])
    print(''.join(text_origen))