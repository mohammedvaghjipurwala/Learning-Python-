a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#print ([x for x in [y ** 2 for y in range(1,11)] if x % 2 == 0])
print ([x for x in [y for y in a] if x % 2 == 0])
