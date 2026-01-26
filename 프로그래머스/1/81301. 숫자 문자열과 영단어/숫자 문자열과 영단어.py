def solution(s):
    word_to_digit = {"zero":0,"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    answer = ""
    t = ""
    for i in s:
        if i.isdigit():
            answer += str(i)
        else:
            t += i
        if t in word_to_digit:
            answer += str(word_to_digit.get(t))
            t = ""

    return int(answer)