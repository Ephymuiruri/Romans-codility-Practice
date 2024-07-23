def func(A, N, B, M):
    seta = set(A)
    print(f"setA {seta}, from Array {A}")
    setb = set(B)
    print(f"setB {setb} from Array {B}")
    setc = seta & setb
    print(f"intersection {setc}")
    return min(setc) if setc else  -1

A = [3, 4, 5]
B = [1, 4, 5, 9]
N = len(A)
M = len(B)

print(func(A, N, B, M))