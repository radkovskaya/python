# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# def my_round(number, ndigits):
#     result = (number*10**ndigits)//1/10**ndigits
#     return result
#
# print(my_round(2.1234567, 5))
# print(my_round(2.1999967, 5))
# print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# def lucky_ticket(ticket_number):
#     ticket_number = str(ticket_number)
#     if len(ticket_number) == 6:
#         if (int(ticket_number[0:1]) + int(ticket_number[1:2]) + int(ticket_number[2:3])) ==(int(ticket_number[3:4]) + int(ticket_number[4:5]) + int(ticket_number[5:6])):
#             result = "счастливый"
#         else:
#             result = "несчастливый"
#     else:
#         result = "необходимо ввести шестизначный номер билета"
#     return result
#
#
# print(lucky_ticket(123006))
# print(lucky_ticket(12321))
# print(lucky_ticket(436751))