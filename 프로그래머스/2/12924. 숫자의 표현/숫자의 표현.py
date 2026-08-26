def solution(n):
    answer = 0
    t = 0

    if n == 1:
        return 1
    
    while True:
        sumNumber = 0
        t +=1
        for i in range(t, n):
            sumNumber += i
            if sumNumber == n:
                answer += 1
                break
            elif sumNumber > n:
                break
        if t == (n//2):
            break
    return answer+1
