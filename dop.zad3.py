def calculate_structure_sum(*args):
    count = 0
    for i in args:
        if isinstance(i,int): # проверка на числа
            count += i
        elif isinstance(i, str): # на строки
            count += len(i)
        elif isinstance(i, dict): # на словарь
            count += calculate_structure_sum(*i.keys()) # обработка ключей
            count += calculate_structure_sum(*i.values()) # обработка значений
        elif isinstance(i, (tuple, list, set) ): # рекурсия для остальных элементов
            count += calculate_structure_sum(*i)
    return count
data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(*data_structure))
