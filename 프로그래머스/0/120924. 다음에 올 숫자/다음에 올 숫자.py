def solution(common):
    answer = []
    if (common[1] - common[0]) == (common[2] - common[1]):
        # 등차 수열일 때
        d = common[1] - common[0]
        answer.append(common[-1]+d)
    elif (common[1] // common[0]) == (common[2] // common[1]):
        r = common[1] // common[0]
        answer.append(common[-1]*r)

    return answer[-1]