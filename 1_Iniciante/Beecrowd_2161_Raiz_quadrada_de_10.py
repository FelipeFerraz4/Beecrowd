def raiz10(times):
    if times == 0:
        return 6
    else:
        div = 6 + (1/raiz10(times-1))
        return div

times = int(input())
raiz = raiz10(times)

print(f'{raiz-3:.10f}')
