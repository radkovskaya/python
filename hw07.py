#!/ usr / bin / python3

# """
# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
#  Если цифра есть на карточке - она зачеркивается и игра продолжается.
#  Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
#  Если цифра есть на карточке - игрок проигрывает и игра завершается.
#  Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y / n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# случайные: http://docs.python.org/3/library/random.html
#
from random import randint, sample, choice

def random_num():
    nums = sample(range(1,91), 15)
    nums1 = sorted(nums[0:5])
    nums2 = sorted(nums[5:10])
    nums3 = sorted(nums[10:15])
    return nums1, nums2, nums3

def random_index_list():
    return sorted(sample(range(0,9), 5))

def create_row(num, index_list):
    row = [0]*9
    for i, index in enumerate(index_list):
        row[index] = num[i]
    return row

def gen_num(barrels):
    i = randint(0, len(barrels)-1)
    gen_num = barrels[i]
    del barrels[i]
    return gen_num

def compare_bitwise(x, y):
    set_x = frozenset(x)
    set_y = frozenset(y)
    return set_x & set_y

barrels = [el for el in range(1,91)]
a, b, c = random_num()
d, e, f = random_num()
card_pl = [create_row(a, random_index_list()), create_row(b, random_index_list()), create_row(c, random_index_list())]
card_comp = [create_row(d, random_index_list()), create_row(e, random_index_list()), create_row(f, random_index_list())]
count = len(barrels)
health_comp = 15
health_pl = 15

while (health_comp != 0 and health_pl != 0):
    count_num = 0
    print("Осталось ячеек у игрока: ", health_pl)
    print("Осталось ячеек у компьютера: ", health_comp)
    num_barrel = gen_num(barrels)
    print("Новый боченок: {}. Количество оставшихся боченков: {}".format ((num_barrel), len(barrels)))
    print("-----Ваша карточка-----")
    for row in card_pl:
        print(row)
    print("-----Карточка компьютера-----")
    for row in card_comp:
        print(row)
    print("Зачеркнуть цифру? (y / n)")
    answer = input()
    while answer not in ["n", "y"]: # Проверка на корректность ввода ответа
        print("Недопустимый символ, можно вводить только y или n. Введите верный символ")
        answer = input()
    if answer == "y": # Если пользователь решил зачеркнуть число
        for row in card_pl: # Построчная проверка наличия "боченка" в карточке игрока
            if row.count(num_barrel) > 0: # Если "боченок" есть в строке
                i = row.index(num_barrel) # Вычисляем индекс элемента "боченка"
                row[i] = None #Заменяем элемент "боченок" на None
                health_pl -= 1
                count -= 1# Уменьшаем счетчик на 1
                continue
            else:
                count_num +=1 #Если "боченка" в строке нет, то увеличиваем счетчик проверок строки на 1
        if count_num == 3: #Проверка 3х строк на наличие "боченка" показала, что "боченка"  в них нет
            print("Вы програли. Искомого числа не было на карточке") #Пользователь ошибся в вводе, пользователь проиграл
            health_comp = 0
            break
        for row in card_comp: #Построчная проверка наличия "боченка" в карточке компьютера
                 if row.count(num_barrel) > 0: #Если "боченок" есть в строке
                    i = row.index(num_barrel)  #Вычисляем индекс элемента "боченка"
                    row[i] = None #Заменяем элемент "боченок" на None
                    health_comp -=1
    if answer == "n":#Если пользователь решил не зачеркивать число
        for row in card_pl: # Построчная проверка наличия "боченка" в карточке игрока
            if row.count(num_barrel) > 0: # Если "боченок" есть в строке
                count_num +=1 #Если "боченок", то увеличиваем счетчик проверок строки на 1
            if count_num > 0: # В случае, если счетчик больше 0, т.е. в одной из строк есть "боченок
                print("Вы проиграли, игра завершена. Искомый боченок был на карточке.") #Пользователь ошибся в вводе, пользователь проиграл
                health_comp = 0
                break # Завершаем цикл
            else:
                for row in card_comp: #Построчная проверка наличия "боченка" в карточке компьютера
                         if row.count(num_barrel) > 0: #Если "боченок" есть в строке
                            i = row.index(num_barrel) #Вычисляем индекс элемента "боченка"
                            row[i] = None #Заменяем элемент "боченок" на None
                            health_comp -= 1

if health_comp == 0 :
    print("Победа компьютера")
elif health_pl == 0 :
    print("Победа игрока")


