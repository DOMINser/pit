#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
s1=len(a)
s2=len(b)
c=[]
for x in range(0,s1):
    y=0
    for y in range(0,s2):
        if a[x]==b[y]:
            c=c+[a[x]]
print(list(set(c)))