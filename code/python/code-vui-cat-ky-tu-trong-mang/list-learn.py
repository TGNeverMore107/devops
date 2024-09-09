n = int(input("nhap so luong cac phan tu trong mang la: 999"))
lst = []
for i in range(n):
    lst.append(int(input("phan tu thu " + str(i+1) + " la:")))

answer = 0
for v in lst:
    answer += v

print(answer)