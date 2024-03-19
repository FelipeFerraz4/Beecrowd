def raiz10(times):
    if times == 0:
        return 2
    else:
        div = 2 + (1/raiz10(times-1))
        return div

times = int(input())
raiz = raiz10(times)

print(f'{raiz-1:.10f}')
