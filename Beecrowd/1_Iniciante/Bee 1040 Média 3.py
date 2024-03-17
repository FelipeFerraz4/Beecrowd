value = input().split()
a, b, c, d = float(value[0]), float(value[1]), float(value[2]), float(value[3])

mean = ((a * 2) + (b * 3) + (c * 4) + d)/10.0

if mean >= 7:
    print(f'Media: {mean:.1f}')
    print('Aluno aprovado.')
elif mean < 5:
    print(f'Media: {mean:.1f}')
    print('Aluno reprovado.')
else:
    print(f'Media: {mean:.1f}')
    print('Aluno em exame.')
    new_test = float(input())
    mean = (new_test+mean)/2.0
    print(f'Nota do exame: {new_test:.1f}')
    if mean >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')

    print(f'Media final: {mean:.1f}')