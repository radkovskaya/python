# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

# def fibonacci(n, m):
#     i = 1
#     x = 0
#     y = 1
#     fib = [1,]
#     while i < m:
#         z = x + y
#         fib.append(z)
#         i +=1
#         x = y
#         y = z
#     return fib[n-1:m]
#
# print(fibonacci(6,15))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# def sort_to_max(origin_list):
#     i = 0
#     х = 0
#     for element in origin_list:
#         while i < len(origin_list)-1:
#             if origin_list[i] > origin_list[i+1]:
#                 x = origin_list[i]
#                 origin_list[i] = origin_list[i+1]
#                 origin_list[i+1] = x
#             i +=1
#         i = 0
#     print(origin_list)
#
# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
# def my_filter (filter_func, lst):
#     i = 0
#     my_list = []
#     while i < len(lst):
#         if filter_func(lst[i]):
#             i +=1
#         else:
#             my_list.append(lst[i])
#             i +=1
#     return my_list
#
# print(my_filter(lambda x : x > 5 , [ 2 , 10 , - 10 , 8 , 2 , 0 , 14 ]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


# def par_lines (x1, y1, x2, y2, x3, y3, x4, y4):
#     return ((x2 - x1 == x3 - x4 and y2 - y1 == y3 - y4 and x2 - x3 == x1 - x4 and y2 - y3 == y1 - y4) or
#             (x2 - x4 == x1 - x3 and y2 - y4 == y1 - y3 and x1 - x2 == x3 - x4 and y1 - y2 == y3 - y4) or
#             (x1 - x2 == x3 - x4 and y1 - y2 == y3 - y4 and x1 - x3 == x2 - x4 and y1 - y3 == y2 - y4) or
#             (x1 - x3 == x2 - x4 and y1 - y3 == y2 - y4 and x3 - x2 == x1 - x4 and y3 - y2 == y1 - y4)
#             )
#
# if par_lines (0, 0, 1 ,1, 2, 1, 1, 0):
#     print("Вершины параллелограмма")
# else:
#     print("Не вершины параллелограмма")