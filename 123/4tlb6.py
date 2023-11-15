import random
n=int(input())
a=[]
for i in n:
    a=list(random.randint(0,100))+a
a=list(a)
mx=a[0]
mn=a[0]
nmn=0
xmn=0
for i in range(0,len(a)):
    if mx<a[i] and mx!=a[i]:
        mx=a[i]
        nmx=i
    if mn>a[i] and mn!=a[i]:
        mn=a[i]
        nmn=i
print(mx,nmx,mn,nmn)
