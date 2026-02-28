# 1 1 1 2(1+1) 2(1+1) 3(1+2) 4(1+3) 5(1+4) 7(2+5) 9(2+7) 12(3+9) 16(4+12) 21(5+16)
import sys

n = int(sys.stdin.readline())

# def waves_sequence(n):
#     if n <= 3:
#         return 1
#     elif n == 4 or n == 5:
#         return 2
#     else:
#         return waves_sequence(n-5) + waves_sequence(n-1)
# 
# for _ in range(n):
#     t = int(sys.stdin.readline())
#     print(waves_sequence(t))

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6, 101):
    dp[i] = dp[i-5] + dp[i-1]

for _ in range(n):
    t = int(sys.stdin.readline())
    print(dp[t])

