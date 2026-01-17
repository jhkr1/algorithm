def solution(code):
    answer = ''
    mode = '0'
    for i in range(len(code)):
        if code[i] == '1':
            if mode == '0':
                mode = '1'
            else:
                mode = '0'
            continue
        if (i == 0 or i % 2 == 0) and mode == '0':
            answer += code[i]
        elif (i % 2 == 1) and mode == '1':
            answer += code[i]
    if answer == '':
        answer = 'EMPTY'

    return answer