calls = 0

def count_calls ():
    global calls           # перевод в глобал, и создание счетчика.
    calls +=1


def string_info (string):
    count_calls()                                       # счетчик, перевод в регистры, длина
    return len(string), string.lower(), string.upper()

def is_contains (string, list_to_search) :
    count_calls()                                        # счетчик, перевод строки в нижний рег, перевод списка в нижний рег, поиск str в lits
    string_lower = string.lower()
    list_lower = [ item.lower () for item in list_to_search ]
    return string_lower in list_lower


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclci']))

# общее количкство вызовов
print(calls)

