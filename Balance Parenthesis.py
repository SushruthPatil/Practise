l = ['[','(','{']
r = [']',')','}']
def check(str):
    stack = []
    for i in str:
        if i in l:
            stack.append(i)
        elif i in r:
            pos = r.index(i)
            if stack and l[pos] == stack[-1]:
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"

str = "{{[()]}}"
print(check(str))