s = { 1, 3, "hello", 5, 7, 9 }
print(s, type(s))
s.remove(3) #remove 3 from set
print(s)

s1 = { 1, 3, 5, 7, 9 }
s2 = { 2, 4, 5, 6, 8, 10 }
print(s1.union(s2)) #union of two sets
print(s1.intersection(s2)) #intersection of two sets