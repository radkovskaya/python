# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

# КОД:
# fruits = ["яблоко", "банан", "киви", "арбуз"]
# i = 0
# while i < len(fruits):
#     print('{}. {}'.format(i, fruits[i]))
#     i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

# Первый вариант:
# first_list = [7, 2, 7, 8, 15, 4]
# second_list = [7, 8]
# i = 0
# j = 0
#
# while i < len(first_list):
#     j = 0
#     while j < len(second_list):
#         print(i, j)
#         if first_list[i] == second_list[j]:
#             first_list.pop(i)
#             i -= 1
#             break
#         j += 1
#     i += 1
# print(first_list)

# Второй вариант:
# first_list = [7, 2, 7, 8, 15, 4]
# second_list = [7, 8]
# i = 0
# j = 0
# while i < len(first_list):
#     for second in second_list:
#         if first_list[i] == second:
#            first_list.pop(i)
#             i -= 1
#             break
#    i += 1
# print(first_list)

# Третий вариант:
# first_list = [7, 2, 7, 8, 15, 4]
# second_list = [7, 8]
# i = 0
# while i < len(first_list):
#     if first_list[i] in second_list:
#         first_list.pop(i)
#     else:
#         i += 1
# print(first_list)



# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

#КОД:
# random_list = [1, 6, 8, 0, 9, 10]
# new_list = []
# for element in random_list:
#     if element%2 == 0:
#         new_list.append(element/4)
#     else:
#         new_list.append(element*2)
# print(new_list)