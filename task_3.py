"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.
"""

for word in ['attribute','класс','функция','type']:
    try:
        print(word,type(word),word.encode('ascii'), ' - encoding to bytes successful ')
    except:
        print(word,type(word),' - not valid input for bytes string')