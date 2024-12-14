from fake_math import divide as fm
from true_math import divide as tm
result1 = fm(69, 3)

result2 = fm(3, 0)

result3 = tm(49, 7)

result4 = tm(15, 0)

print(result1)  # Ожидаем 23.0
print(result2)  # Ожидаем "Ошибка"
print(result3)  # Ожидаем 7.0
print(result4)  # Ожидаем "inf"