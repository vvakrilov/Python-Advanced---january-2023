expression = input()
s = []  # solution stack will get expression indexes
for i in range(len(expression)):
    ch = expression[i]
    if ch == "(":
        s.append(i)
    elif ch == ")":
        p = s.pop()
        print(expression[p:i + 1])  # +1 to include last stack item when slicing
