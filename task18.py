#Посчитайте, сколько раз символ встречается в строке.
a=str(input())
sim=str(input())
a=list(a)
print(a)
vsego=0
for i in range(len(a)):
    if sim==a[i]:
        vsego+=1
print(vsego)

