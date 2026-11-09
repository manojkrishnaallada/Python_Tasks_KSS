#find common elements, elements only in the first list, and all unique elements.

l1 = [1,2,3,4,5]
l2 = [3,4,5,6,7]
s1 = set(l1)
s2 = set(l2)
print(s1 & s2)
print(s1 - s2)
print(s1 | s2)
