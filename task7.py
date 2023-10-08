#Нужно вывести первые n строк треугольника Паскаля. В этом треугольнике на вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел.
n=int(input())
spis=[]
for i in range(n+1):
     spis.append([1]+[0]*n)
for i in range (1,n+1):
     for j in range (1,n+1):
         spis[i][j]=spis[i-1][j]+spis[i-1][j-1]
for i in spis:
    print(i)
     