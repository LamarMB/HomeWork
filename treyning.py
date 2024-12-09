def ancient_cipher(n):
    result = ''  # Финальный пароль

    for i in range(1 , n):
        for num in (i +1, n +1 ):
            sum = i + num
            if i % num == 0 :
                result += f'{i}{num}'
    return result


n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = ancient_cipher(n)
    print(f"Результат для числа {n}: {result}")
else:
    print("Число должно быть от 3 до 20!")


 
