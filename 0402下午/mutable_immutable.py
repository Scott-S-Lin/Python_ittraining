list1 = [1,2,3,'apple']
list1[0] = 99

list2 = [2,4,6,[11,22,33],list1]
print(list2[4] is list1)
print(id(list1))
print(id(list2))
print(id(list2[4]))
print(id(list2[3]))
'''
list1 = [1,2,3,'apple']
list2 = [2,4,6,[11,22,33],list1]
list2[4][0] = 99
list[1] = 88
'''
