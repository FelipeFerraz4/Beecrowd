while True:
    try:
        number = int(input())
        e1, e2 = map(int, input().split())
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        if number == 1:
            x1, x2 = map(int, input().split())
            resultado = min(e1 + a1[0] + x1, e2 + a2[0] + x2)
            print(resultado)
            continue
        
        t1 = list(map(int, input().split()))
        t2 = list(map(int, input().split()))
        x1, x2 = map(int, input().split())
        
        dp1 = [0] * number
        dp2 = [0] * number
        
        dp1[0] = e1 + a1[0]
        dp2[0] = e2 + a2[0]
        
        for i in range(1, number):
            dp1[i] = a1[i] + min(dp1[i - 1], dp2[i - 1] + t2[i - 1])
            dp2[i] = a2[i] + min(dp2[i - 1], dp1[i - 1] + t1[i - 1])
        
        result = min(dp1[number - 1] + x1, dp2[number - 1] + x2)
        print(result)
        
    except EOFError:
        break