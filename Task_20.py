# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

def scrabble(dictionary, word):
    keys = word.upper()
    word_cost = 0
    for i in keys:
        word_cost += dictionary.get(i, 0)
    return word_cost

def create_dictionary(language, points):
    dictionary = dict()
    for k, v in zip(language, points):
        dop = dict.fromkeys(k, v)
        dictionary.update(dop)
    return dictionary

def identify_language(string):
    if set(string).issubset(set(english)):
        return (eng, string)
    elif set(string).issubset(set(russian)):
        return (rus, string)
    else:
        # print('Некорректный ввод! Пожалуйста повторите ввод!')
        word = input('Введите другое слово на русском или английском, это слово написано неправильно: ')
        return (False, word)
      

e1 = 'AEIOULNSTR'
e2 = 'DG'
e3 = 'BCMP'
e4 = 'FHVWY'
e5 = 'K'
e8 = 'JX'
e10 = 'QZ'

r1 = 'АВЕИНОРСТ'
r2 = 'ДКЛМПУ'
r3 = 'БГЁЬЯ'
r4 = 'ЙЫ'
r5 = 'ЖЗХЦЧ'
r8 = 'ШЭЮ'
r10 = 'ФЩЪ'

russian = r1 + r2 + r3+r4+r5+r8+r10
english = e1 + e2 + e3+e4+e5+e8+e10
eng = (e1, e2, e3, e4, e5, e8, e10)
rus = (r1, r2, r3, r4, r5, r8, r10)
points_set = (1, 2, 3, 4, 5, 8, 10)

word = input('Введите слово на русском или английском : ')

language = False
result = (language, word)

while result[0] == False:
    result = identify_language(word.upper())
    language, word = result
    
dictnry = create_dictionary(language, points_set)
print(f'Всего {scrabble (dictnry, word)} баллов!\n')