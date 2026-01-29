def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0] - 1
        end = command[1]
        idx = command[2] - 1
        array_sorted = sorted(array[start:end])
        if len(array_sorted) != 1:
            answer.append(array_sorted[idx])
        else:
            answer.append(array_sorted.pop())
    return answer
