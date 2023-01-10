solution_stack = []
lines_count = int(input())
for _ in range(lines_count):
    query = input()
    if query[0] == 1:
        _, value = query.split()
        solution_stack.append(value)
        pass
