# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2

import random

N = int(input('Введите размер массива N: '))
X = int(input('Введите число X: '))
mass = []
for i in range(N):
    mass.append(random.randint(0, N//2))

count = 0
for i in mass:
    if i == X:
        count += 1
print(f'Получившийся массив: {mass}')
print(f'Число {X}, встречается {count} раз в массиве')
     
for i in mass:
    if X > N:
        print('Некорректный ввод. Попробуйте еще раз!')
        break
       