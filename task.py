a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
al=len(a)
t=0

while al>0:
    if a[t]<5:
        print(a[t])
    t=t+1
    al=al-1
    