jewelry = {}
while True:
    try:
        text = input()
        if text not in jewelry:
            jewelry[text] = 1
    except EOFError:
        print(len(jewelry))
        break