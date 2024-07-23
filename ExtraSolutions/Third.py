def solution(A, N, B, M):
    A.sort()
    B.sort()

    i, j = 0, 0


    min_common_value = None


    while i < N and j < M:
        print(A[i],i, B[j],j)
        if A[i] == B[j]:
            if min_common_value is None or A[i] < min_common_value:
                min_common_value = A[i]
            i += 1
            j += 1
        elif A[i] < B[j]:
            print(A[i],i)
            i += 1
        else:
            j += 1


    if min_common_value is None:
        return -1
    else:
        return min_common_value
    

A =[1,3,2,1]
B =[4,2,5,3,2]
print(solution(A,len(A),B,len(B)))

