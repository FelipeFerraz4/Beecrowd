from sys import stdin

def find_host(n, elves):
    elves.sort()
    largest = elves[-1]
    
    # Conjunto de múltiplos dos elfos (descarta o primeiro e limita a 20 elementos)
    multiples = set()
    for elf in elves[1:min(len(elves), 20)]:
        start = (largest // elf + 1) * elf  # Calcula o primeiro múltiplo maior que 'largest'
        for multiple in range(start, largest + 500, elf):
            multiples.add(multiple)

    multiples = sorted(multiples)
    
    candidate = largest + 1

    # Encontra o menor número maior que 'largest' que não está na lista de múltiplos
    for multiple in multiples:
        if candidate == multiple:
            candidate += 1
        elif candidate < multiple:
            break

    return candidate


if __name__ == "__main__":
    number_of_elves = int(stdin.readline())
    elf_identifiers = list(map(int, stdin.readline().split()))
    
    host = find_host(number_of_elves, elf_identifiers)
    print(host)
