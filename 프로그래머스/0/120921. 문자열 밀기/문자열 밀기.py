def solution(A, B):
    answer = 0
    temp = ''
    for i in range(len(A)):
        if (A == B):
            return answer
        else:
            temp = A[-1] + A[:-1]
            answer += 1
            A = temp

    return -1