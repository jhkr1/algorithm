def solution(s, n):
    result = []

    for ch in s:
        # 소문자 처리
        if 'a' <= ch <= 'z':
            shifted = chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
            result.append(shifted)

        # 대문자 처리
        elif 'A' <= ch <= 'Z':
            shifted = chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
            result.append(shifted)

        # 알파벳이 아니면 그대로
        else:
            result.append(ch)

    return ''.join(result)