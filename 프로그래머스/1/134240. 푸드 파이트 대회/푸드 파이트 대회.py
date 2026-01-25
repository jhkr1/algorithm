def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i] >= 2 and food[i] % 2 == 0:
            # 짝수인 경우
            t = food[i] // 2
            answer += str(i) * t

        elif food[i] >= 2 and food[i] % 2 != 0:
            t = (food[i] // 2)
            answer += str(i) * t

    answer += '0'
    answer += answer[-2::-1]

    return answer