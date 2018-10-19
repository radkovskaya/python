# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

# line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlezcsgamkgayeomhbsqssuhkvsfbmxulaysmno'\
#        'GIPHpEMujalpPLNzRWXfwHQqwksrFeipeultleclmwaoktklfubjhpsnawvjphfgewvzk'\
#        'TUfSYtBydXaVIpxWjNKgXANvIoumesCSsvjegrjosufuhrrduutqwlljjjddkvjfsahqn'\
#        'LxooisBDWuxIhyjJaXDYwdoVPnsllMngnlmkpyolqxefixpqqqgawdjsovqppofyivjxa'\
#        'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvzgkdoaqylvbfsgsafjmchgbwasgnbnwete'\
#        'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyqrzouyhkxrkdyiebvtjdbycfkviaqaabfcvzq'\
#        'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwpfkapxgqnzcvffkrluigblowhchwcdjbruxb'\
#        'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeymdevhhbjmbsshdqbjaudgttrsxzywykmjcc'\
#        'EUZShGofaFpuespaZWLFNIsOqsIRLexWqtxsoascgnsuksjxiihwscdbvieqbhqaonlfb'\
#        'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwtvazmutmsqqzghlmqkjndiaxbizvkgseut'\
#        'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZghfizjwtzcexzcnzjlemiflxnpkqfjfbcfkcu'\
#        'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCbxbgvqhmlsszmwsvqyzenwogxygpvbnhwhuxb'\
#        'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxlnqosbdgvnuyeziheapqgoxwexolwidqnjfa'\
#        'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnvjxpfizvddylexylnkbflcjlhntltignbqoiq'\
#        'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# import re
# if re.search(r'[A-Z]+', line) is None:
#     result = []
# else:
#     result = re.split(r'[A-Z]+', line)
# print(result)
#
# lst = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# j = 0
# i = 0
# my_list = []
# while i < len(line):
#     if line[i] in lst:
#         str = line[j:i]
#         j = i + 1
#         if str != '':
#             my_list.append(str)
#     i += 1
# if line[j:i] != '' and j > 0:
#     my_list.append(line[j:i])

# print(my_list)


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

# line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlezcsgamkgayeomhbsqssuhkvsfbmxulaysm'\
#        'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipeultleclmwaoktklfubjhpsnawvjphfgewv'\
#        'fzKTUfSYtBydXaVIpxWjNKgXANvIoumescssvjegrjosufuhrrduutqwlljjjddkvjfsa'\
#        'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllmngnlmkpyolqxefixpqqqgawdjsovqppofyiv'\
#        'jXapzGOrfinzzsNMtBIOclwbfRzytmDgefuzxvzgkdoaqylvbfsgsafjmchgbwasgnbnw'\
#        'etekUTVuPluKRMQsdelzBgLzuwiimqkFkpyqrzouyhkxrkdyiebvtjdbycfkviaqaabfc'\
#        'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoqnswpfkapxgqnzcvffkrluigblowhchwcdjbr'\
#        'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZwjueymdevhhbjmbsshdqbjaudgttrsxzywykm'\
#        'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexwqtxsoascgnsuksjxiihwscdbvieqbhqaon'\
#        'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpguflwtvazmutmsqqzghlmqkjndiaxbizvkgs'\
#        'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurzghfizjwtzcexzcnzjlemiflxnpkqfjfbcf'\
#        'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXescbxbgvqhmlsszmwsvqyzenwogxygpvbnhwh'\
#        'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyywxlnqosbdgvnuyeziheapqgoxwexolwidqn'\
#        'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeknvjxpfizvddylexylnkbflcjlhntltignbq'\
#        'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxgc'
# import re
# my_list = re.findall(r'[a-z]{2,2}[A-Z]+[A-Z]{2,2}', line_2)
# new_list = [el[2:-2] for el in my_list]
# print(new_list)


# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.


# import random
# import string
# my_file = open("some.txt", "w")
# string = (''.join(random.choice(string.digits) for i in range(2500)))
# my_file.write(string)
# print(string)
#
# def count_max (string):
#        count_max = 0
#        i = 0
#        count = 0
#        while i < len(string) - 1:
#               if string[i] == string[i+1]:
#                      count +=1
#                      if count_max < count:
#                             count_max = count
#               else:
#                      count = 0
#               i +=1

#        return count_max
#
# print(count_max(string))


