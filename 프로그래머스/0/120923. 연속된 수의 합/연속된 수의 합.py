def solution(num, total):
    x = int((total / num) - (num-1)/2)
    return [x + i for i in range(num)]
