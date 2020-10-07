set1 = {x for x in range(10)} 
set2 = {'a','b', 'c', 'd',1, 2, 3}

print (set1.union(set2))

print(set1.intersection(set2))

print(set1.difference(set2))
print(set2.difference(set1))
#same resolt for the symmetric_difference
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))