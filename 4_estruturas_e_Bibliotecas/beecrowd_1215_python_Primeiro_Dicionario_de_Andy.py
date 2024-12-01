import re

andy_dict = set()

while True:
    try:
        text = input().strip()
        
        if not text:
            continue
        
        cleaned_text = re.sub(r'[^a-zA-Z]', ' ', text.lower())

        words = cleaned_text.split()

        andy_dict.update(words)
        
    except EOFError:
        for word in sorted(andy_dict):
            print(word)
        break