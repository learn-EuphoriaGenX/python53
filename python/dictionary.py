# list == dictiory ~True
# ordered, changable, no duplicate, 
lst = [10,20,30,40, 50]
dct = {'one':10, 'two':20,  'three':30, 'four':40, 'five':50, 'four':40}
# print(len(dct))
print(lst[0])
dct['four'] = 400
dct['my_array'] = ["hello" , "my", "name", "is", "..."]


myKeys = ('zero', 'one', 'two')
value = 80
mydict = dict.fromkeys(myKeys, value)
mydict.update({'zero': 0})
mydict.update({'one': 1})
mydict.update({'two': 2})
print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(mydict)



