immutable_var=[3, 5, True, 'Lox']
print(immutable_var)
# Кортежи неизменяемые так, потому что (прочитал в инете) : 1. Оптимизация производительности,быстрее обрабатывется.
# 2. Безопасность данных, защита от случайных изменений. 3. Простота и предсказуемость.

mutable_list=([3, 5, True ],'Lox')
print(mutable_list)
mutable_list= (mutable_list [0], 'sam Lox')
print(mutable_list)
mutable_list [0] [1]=4
print(mutable_list)