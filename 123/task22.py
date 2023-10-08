from collections import Counter
#напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
file=open( r'C:\Users\79287\Desktop\git\pit-1\123\125.txt',encoding='utf-8') 
a=str(file.read())
a=a.split( )
c=Counter(a)
print(c)
print( )
print(c.most_common(2))



