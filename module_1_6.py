my_dict = {"papich": 1654,"semadog": 627,"vika": 1923}
print(my_dict)
print(my_dict['vika'], my_dict.get('vasya'))
my_dict.update({'bogdan': 2000,
               'artstyle': 1783})
del my_dict['vika']
print(my_dict)

my_set={1, 2, 2, True, 'dada', False}
print(my_set)
my_set.add(None)
my_set.add(3)
print(my_set)
my_set.remove(3)
print(my_set)