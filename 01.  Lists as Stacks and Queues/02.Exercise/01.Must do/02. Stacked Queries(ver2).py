from collections import deque

numbers = deque()

map_functions = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(max(numbers)) if numbers else None,
}

for _ in range(int(input())):
    numbers_data = [
        int(x) for x in input().split()
    ]
    map_functions[numbers_data[0]](numbers_data)

numbers.reverse()
print(*numbers, sep=', ')
