import sys

n = int(sys.stdin.readline())

# N=1일 때 index error 방지를 위해 n+2 길이로 초기화
dp = [0] * (n + 2)

dp[1] = 1
dp[2] = 3

# N이 3 이상일 때 새로운 점화식 적용
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007

print(dp[n])