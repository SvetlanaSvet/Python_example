#k = input('Введите слово: ').upper()
k = 'lizard'
k = k.upper()

eng_alph = 'QWERTYUIOPASDFGHJKLZXCVBNM'
rus_alph = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'

flag = bool

if len([i for i in k if i in eng_alph]) == len(k): flag = False
elif len([i for i in k if i in rus_alph]) == len(k): flag = True
else: print('Проверьте введенные данные')

# len([i - в i посчитаем длину слова (если 0, то у нас такого алфавита нет)
# for i in k  - от первой до последней буквы слова 
# if i in eng_alph - есть ли буква в алфавите
# если пользователь правильно ввел слово (буквы из одного алфавита), то 
# длина вхождения в алфавит д.б. равна длине слова

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

if flag:
    print(sum([key for i in k for key, v in rus.items() if i in v]))
else:
    print(sum([key for i in k for key, v in eng.items() if i in v]))

# sum([key - складываем значения ключей
# for i in k - от первой до последней буквы слова 
# for key, v in rus.items() - проходим по ключам и значениям словаря
# if i in v] - если буква вошла в значение