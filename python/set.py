# Unordered, Unchangeable, Duplicates Not Allowed

setA = {10, 20, 30, 40, 50}
setB = {15, 20, 25, 30, 35}
print(type(setA))
print(setB)

print(setA.difference(setB)) # 40, 50, 10 - difference
print(setA.intersection(setB)) # 20, 30 - common element
print(setA.union(setB)) # addition
print(setB.issubset(setA)) # <=
print(setA.issuperset(setB)) # >=
setA.pop() # remove last element
setA.remove(10) # remove specific element