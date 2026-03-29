import sys

input = sys.stdin.readline
expression = input().strip()
parts = expression.split('-')
result = sum(map(int, parts[0].split('+')))

for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

print(result)