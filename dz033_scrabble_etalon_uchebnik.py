# Решение задачи Скрабл:
# https://proglib.io/p/slovari-v-python-12-zadach-dlya-nachinayushchih-s-resheniyami-2022-01-28
# Сначала напишем функцию isCyrillic(), которая возвращает True,
# если введенное слово содержит кириллические символы, и False, если буквы – латинские.

# Затем создадим словари, где ключами будут очки, а значениями – строки из букв.
# Метод items() позволяет обращаться к ключам и значениям одновременно – если очередная буква 
# в слове входит в одно из значений, генератор добавит ключ в список,
# а метод списка sum() подсчитает стоимость всего слова

import re

def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))

eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JX',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}

text = input('Введите слово: ').upper()

if isCyrillic(text):
	print(sum([k for i in text for k, v in rus.items() if i in v]))
else:
	print(sum([k for i in text for k, v in eng.items() if i in v]))