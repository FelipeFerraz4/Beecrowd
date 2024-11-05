number = int(input())
if number >= 3:
    dp = [0 for i in range(number + 1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, number + 1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % (10**9 + 7)
    print(dp[number])
elif number == 2:
    print(2)
else:
    print(1)
    