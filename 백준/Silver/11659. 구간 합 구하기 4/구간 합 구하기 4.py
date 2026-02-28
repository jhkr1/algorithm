# 수의 개수 n과 합을 구해야하는 횟수 m
# 둘째 줄 n개의 수, n <= 1000
# 셋째 줄 ~ m개의 줄에는 합을 구해야한느 구간 i와 j

import sys

n,m = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))

# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     result =0
#     for j in range(a-1, b):
#         result += t[j]
#     print(result)

# 누적합 저장 배열
prefix_sum = [0]
temp = 0

for i in t:
    temp += i
    prefix_sum.append(temp)

# print(prefix_sum)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 5 + 4 + 3 -> 12 - 0
    # 4 + 3 + 2  -> 14 - 5
    result = prefix_sum[b] - prefix_sum[a-1]
    print(result)