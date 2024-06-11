n=input()
def duplicates(s):
    result = []
    for char in s:
        if len(result) == 0 or char != result[-1]:
            result.append(char)
    return ''.join(result)
output = duplicates(n)
print(output)
