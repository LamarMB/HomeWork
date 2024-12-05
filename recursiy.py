def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])  # после перевода в строку, преобразуем в инт и берем первую цифру


    if first == 0:
        first = 1   # это чтобы не было обнуления и второй вызов корректно работал
    if len(str_number) > 1 :
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)


