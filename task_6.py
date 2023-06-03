"""
 Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import locale

def_co=locale.getpreferredencoding()
print(def_co)

with open('test_file.txt', 'r', encoding='utf-8') as f:
    for el_str in f:
        print(el_str)
