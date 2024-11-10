my_dict = {'murad':2001, 'kiril': 2015, 'gomer':1412}

my_dict.update({'islaam':2012,
             'sanychlenosos' : 2000})
print(my_dict)
print(my_dict.get('kamila'))
print(my_dict.pop('murad'))
delited_value = my_dict.pop('kiril')
print('kiril:', delited_value)
print(my_dict)



my_set= {1,2,1,2,1,4,5,3,2,1,}
print(my_set)
my_set.update([6,7,8])
print(my_set)
my_set.remove(1)
print(my_set)