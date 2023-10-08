#Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.
a =str(input())
ins = a.split(',')
print(ins,type(ins))
print(tuple(ins),type(tuple(ins)))