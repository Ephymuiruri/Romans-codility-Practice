import itertools
def valid_time(h1, h2, m1, m2):
    hrs = h1 * 10 + h2
    mins = m1 * 10 + m2

    return (hrs >= 0 and hrs <= 23 and mins >= 0 and mins <= 59)

def solution(A, B, C, D):
    count = 0
    digits = [A, B, C, D]
    possibilities = set(itertools.permutations(digits))

    for possibility in possibilities:
        if valid_time(possibility[0], possibility[1], possibility[2], possibility[3]):
            count += 1
    return count

print(solution(6, 2, 4, 7))
print(solution(1,8,3,2))
