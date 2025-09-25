# marks1 = 23
# marks2 = 34
# marks3 = 56
# .
# .
# .

# Ordered, Changeable, Allow Duplicates
marks = [23, 34, 56, 10, 69, 89, 69] # list / array
#        0    1   2   3   4   5   6
# print(marks[0]) # 23
# print(marks[1]) # 34
# print(marks[2]) # 56

print(len(marks))
print(type(marks))
print(marks[-3] == marks[4] )
print(marks[2:5])
print(marks[:5])
print(marks[2:])
marks[3] = 100


marks.append("Apple")
marks.pop()
print(marks.count(69))
print(marks.index(69))
marks.remove(69)

marks.sort()
marks.reverse()
print(marks)
