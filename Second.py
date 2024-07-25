def solution(A):
    A.sort()
    rooms = 0
    i = 0
    N = len(A)

    while i < N:
        rooms += 1
        max_guests = A[i]
        while i < N and max_guests > 0:
            i += 1
            max_guests -= 1
    
    return rooms

print(solution([1, 1, 1, 1, 1]))  
print(solution([2, 1, 4])) 
print(solution([2, 7, 2, 9, 8]))
print(solution([7, 3, 1, 1, 4, 5, 4, 9]))
