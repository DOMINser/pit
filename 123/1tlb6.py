a="Таким образом, начало повседневной работы по формированию позиции в значительной степени обуславливает создание экономической целесообразности принимаемых решений! С другой стороны реализация намеченного плана развития позволяет выполнить важнейшие задания по разработке соответствующих условий активизации? С другой стороны постоянный количественный рост и сфера нашей активности напрямую зависит от новых предложений? Таким образом"
a=list(a)
for i in range(0,len(a)):
    if i>=len(a):
        break
    if a[i]==',' or a[i]=='?' or a[i]=='!' or a[i]=='.':
        del a[i]
a=''.join(a)
a=a.split()
for i in range(0,len(a)):
    a[i]=list(a[i])
Max=0
x=0
mx=0
for i in range(0,len(a)):
    x=len(a[i])
    if x>Max:
        Max=x
        Mx=a[i]
print(''.join(Mx))