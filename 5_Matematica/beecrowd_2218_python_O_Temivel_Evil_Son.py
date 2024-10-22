# Há uma fórmula bem conhecida que permite calcular o número de regiões formadas por 𝑁 retas em posição geral. O número de regiões é dado por:
def number_regions(number_line):
    return ((number_line * (number_line+1)) // 2) + 1 


number_tests = int(input())
for item in range(number_tests):
    test = int(input())
    print(number_regions(test))