def solution(k, score):
    hall_of_fame = []
    answer = []
    for i in score:
        hall_of_fame.append(i)
        hall_of_fame.sort(reverse=True)
        if len(hall_of_fame) <= k:
            answer.append(hall_of_fame[-1])
        else:
            answer.append(hall_of_fame[k-1])
    return answer
