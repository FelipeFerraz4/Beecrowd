numbers_test = int(input())
for i in range(numbers_test):
    phase = input().replace(' ', '').replace(',', '')
    alphabet = []
    for j in range(len(phase)):
        if phase[j] not in alphabet:
            alphabet.append(phase[j])
    if len(alphabet) == 26:
        print("frase completa")
    elif len(alphabet) >= 13:
        print("frase quase completa")
    else:
        print("frase mal elaborada")
    