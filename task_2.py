"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных
"""

first_word = b'class'
second_word = b'function'
third_word = b'method'

print(type(first_word), first_word, len(first_word))
print(type(second_word), second_word, len(second_word))
print(type(third_word), third_word, len(third_word))