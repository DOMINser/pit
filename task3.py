#Отсортируйте словарь по значению в порядке возрастания и убывания.
b={
    1:6,
    3:8,
    5:4,
    7:2
}
print('по возрастанию->')
for i in sorted(b.items(), key=lambda ot: ot[1]):
    print(i)
print('по убыванию->')
for i in sorted(b.items(), key=lambda ot: ot[1],reverse=True):
    print(i)
    