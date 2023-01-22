PUSH_NUMBER = '1'
DELETE_FROM_TOP = '2'
PRINT_MAX_NUM = '3'
PRINT_MIN_NUM = '4'

solution_stack = []
lines_count = int(input())

for _ in range(lines_count):
    query = list(input().split())
    OPERATION = query[0]
    if OPERATION == PUSH_NUMBER:
        value = int(query[1])
        solution_stack.append(value)
    else:
        if solution_stack:
            if OPERATION == DELETE_FROM_TOP:
                solution_stack.pop()
            elif OPERATION == PRINT_MAX_NUM:
                print(max(solution_stack))
            elif OPERATION == PRINT_MIN_NUM:
                print(min(solution_stack))

if solution_stack:
    solution_stack.reverse()
    print(*solution_stack, sep=', ')
else:
    print(solution_stack)