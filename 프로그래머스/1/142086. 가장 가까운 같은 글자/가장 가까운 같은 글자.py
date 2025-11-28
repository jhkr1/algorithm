def solution(s):
    last_pos = {}
    result = []

    for i, ch in enumerate(s):
        if ch in last_pos:
            result.append(i - last_pos[ch])
        else:
            result.append(-1)
        last_pos[ch] = i

    return result
