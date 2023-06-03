# task_1
"""
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
"""
first_word = "разработка"
second_word = "сокет"
third_word = "декоратор"

print(type(first_word), first_word)
print(type(second_word), second_word)
print(type(third_word), third_word)

unicode_first_word = u'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
unicode_second_word = u'\u0441\u043e\u043a\u0435\u0442'
unicode_third_word = u'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

print(type(unicode_first_word), unicode_first_word)
print(type(unicode_second_word), unicode_second_word)
print(type(unicode_third_word), unicode_third_word)