def solution(S):
    stack = []
    MAX_VALUE = (1 << 20) - 1 

    operations = S.split()

    for op in operations:
        if op.isdigit():
            value = int(op)
            if 0 <= value <= MAX_VALUE:
                stack.append(value)
            else:
                return -1
        elif op == "POP":
            if not stack:
                return -1
            stack.pop()
        elif op == "DUP":
            if not stack:
                return -1
            stack.append(stack[-1])
        elif op == "+":
            if len(stack) < 2:
                return -1
            a = stack.pop()
            b = stack.pop()
            result = a + b
            if result > MAX_VALUE:
                return -1
            stack.append(result)
        elif op == "-":
            if len(stack) < 2:
                return -1
            a = stack.pop()
            b = stack.pop()
            result = a - b
            if result < 0:
                return -1
            stack.append(result)
        else:
            return -1

    if not stack:
        return -1

    return stack[-1]

print(solution("4 5 6 - 7 +"))
print(solution("13 DUP 4 POP 5 DUP + DUP + -")) 
print(solution("5 6 + -"))
print(solution("3 DUP 5 - -"))  
print(solution("1048575 DUP +")) 
