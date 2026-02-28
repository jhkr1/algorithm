import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    zero_count = [1, 0]
    one_count = [0, 1]

    if n >= 2:
        for i in range(2, n+1):
            zero_count.append(zero_count[i-2] + zero_count[i-1])
            one_count.append(one_count[i-1] + one_count[i-2])
    print(f"{zero_count[n]} {one_count[n]}")

