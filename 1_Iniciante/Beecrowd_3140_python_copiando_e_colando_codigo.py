run = 0
tags = []
while run != 3:
    text = str(input())
    text2 = text.strip()
    if text2 == '<body>':
        run = 1
    if run == 1:
        tags.append(text)
    if text2 == '</body>':
        run = 2
    if text2 == '</html>':
        run = 3
for i in range(1, len(tags)-1):
    print(tags[i])
