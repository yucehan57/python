# # create a sample dictionary
# # by passing values as an argument
#
# dictionary1 = dict(first_m = 'fight club', second_m = 'dark knight')
# # print(dictionary1)
#
# # because when keys are simple strings, it is easier to create a dictionary
# # by using dict function and by passing its keys as keyword arguments
#
# """Loop through a dictionary"""
#
# for k,v in dictionary1.items(): #items method must be used
#     # print(k, ":", v)
#
# # listed_dict = list(dictionary1) #makes a list of keys
# # print(listed_dict)              #displays only the keys
# # sorted_listed_dict = sorted(listed_dict)
# # print(sorted_listed_dict)       #displays only the keys
#
# # just as list comprehension, we can also use dictionary comprehension
# # key: x itself, value: x to the power of 3
# dict1 = {x:x**3 for x in range(1,15)}
# # print(dict1)
# dict1['y']='Del Piero'
# # print(dict1)
# del dict1['y']
# # print(dict1)
#
# #use a list as a queue
# queue = ['john', 'maverick', 'barnie', 'howie']
# from collections import deque
# queue = deque(['john', 'maverick', 'barnie', 'howie'])
# # print(queue)
# queue.popleft() #drop first arrival and return the value
#
#
# # returns a list in which x**3 and y**3 shown
# sample_list = [(x**2,y**2) for x in range(1,10) for y in range (1,10) if x != y]
# # print(sample_list)
#
# # to loop over two more or sequences at the same time
# # the entries can be paired with the zip() function

statements = ['The number is', 'The color is', 'The USD/TRY rate is']
# answers = ['7', 'Red', '6.66']
# for s, a in zip(statements, answers):
#     print(s, a, ".", end=' ')
