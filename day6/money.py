n, money = map(int, input().split())
moneys = list(map(int, input().split()))

iLen = money + 1
dp = [0] * iLen

for i in range(1, iLen):
    dp[i] = 2**31

for i in range(1, iLen):
    for j in range(n):
        if moneys[j] <= i:
            if dp[i] < dp[i - moneys[j]] + 1:
                dp[i] = dp[i - moneys[j]] + 1
print('min : ', dp[money])
