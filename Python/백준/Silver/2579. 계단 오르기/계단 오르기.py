n = int(input())
s = []
dp = [0] * n

for _ in range(n):
    s.append(int(input()))

dp[0] = s[0]
if n > 1:
	dp[1] = s[0]+s[1]
if n==1:
	print(dp[0])
elif n==2:
	print(dp[1])
else:
	for i in range(2, n):
		if i == 2:
			dp[i] = max(s[i-1]+s[i], dp[i-2]+s[i])
		else:
			dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
	print(dp[n-1])