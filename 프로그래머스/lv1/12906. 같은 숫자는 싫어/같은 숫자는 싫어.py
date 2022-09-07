def solution(arr):
    stack = []
    stack.append(arr[0])
    for i in range(1, len(arr)) :
        if arr[i] != stack[-1] :
            stack.append(arr[i])
    return stack