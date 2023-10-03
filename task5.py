my = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
print(sorted(my, key=my.get, reverse=True)[:3])
