
# #The Syntax for list comprehension
# # newlist = [expression for item in iterable if condition == True]

# lst = ['a','b','c','d','e']
# lst = ['rahim','karim','rakib','nurul','rubel']
# new_lst = [i for i in lst if i.startswith('r')]

# print(new_lst)


# i = 0
# while i < len(lst):
#     print(lst[i].rjust(5))
#     i += 1

# [print(i.rjust(5)) for i in lst]         # list comprehension


# lst = [1,2,3,4,5,6]
# lst = [str(i) for i in lst]
# lst1 = '+'.join(lst)
# print(lst1)