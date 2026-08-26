def solution(n):
    t = n
    n_count = bin(n).count('1')
    while True:
        t += 1 
        t_count = bin(t).count('1')

        if n_count == t_count:
            break
    return t

