string = [ch for ch in input().split()]

solution = []

while string:
    solution.append(string.pop())
print(*solution)
