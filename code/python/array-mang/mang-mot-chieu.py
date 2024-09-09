n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
result = 0
for r in lst:
    result += r
print(result)