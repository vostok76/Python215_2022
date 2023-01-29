# name1 = "Sergey"
#
# print("hello,", name1)
# age = 46
# print(age)

# a = 5
# print(a)
# print(type(a))
# b = "6"
# print(type(b))
# print(b)
# print(a + int(b)) # 56 11

# a = 4
# b = 5
# print(id(a))
#
# a = b
# print(a)
# print(id(a))
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = "2.5"
# print(type(a))

# print("строка символов")
# print('строка символов')

# print('документ "file.py"')
# print("документ \"file.\n py\"")

# s1 = "hello"
# s2 = "python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 5)

# print(86859049586758777777777777755555555555549409)
# print(8.6859049586758777777777777755555555555549409)

# print(6+2)
# print(6-2)
# print(6*2)
# print(6**2)
# print(6/4)
# print(6//4)
# print(6%4)

# a = 5
# b = 7
# c = 3
# summ = a + b + c
# print('сумма равна ', summ)
#
# print('произведение ', a * b * c)
#
# print('среднее арифметическое ', summ / 3)

# number = 6 + 4 * 5 ** 2 + 7
# number1 = (6 + 4) * (5 ** 2 + 7)
# print(number)
# print(number1)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
# num -=3  # num = num - 3
# print(num)  #  12
#
# num *=4
# print(num)

# num = 4321
# print(num)
# a = num % 10
# print("a = ", a)
# num = num // 10
# print(num)
# b = num % 10
# print("b =", b)

#  25.12.2022 занятие 2 PYTHON.


# функции явного преобразования типов:
# int()
# str()
# float()
# bool()

# num1 = "2"
# num2 = 3.5
# res = int(num1) + num2
# print(res)
#
# print(int(-3.891))
#
# a = 3.891
# a = round(a, 2)
# print(a)
# print(type(a))


# num1 = "5.2"
# num2 = 10
# c = float(num1) + num2
# print(c)

# name = "Виктор"
# age = 26
# print("Меня зовут", name, " . Мне", age, "лет.")
# print("Меня зовут " + name, " . Мне " + str(age) + " лет.")
# print("Меня зовут", name, " . Мне", age, "лет.", sep="--", end=" ")
# #  print()
# print("Я учу Python")

# name = input("Ведите имя :")
# print("Вас зовут", name)

# num = int(input("введите число: "))
# power = int(input("введите степень: "))
# # num = int(num)
# # power = int(power)
# num = 5.2
# res = num ** power
# print("число", num, "в степени", power, "равно", res)

# num1 = input("Введите первое число: ")
# num2 = input("Введите второе число: ")
# num3 = input("Введите третье число: ")
# num4 = input("Введите четвёртое число: ")


# b1 = True
# b2 = False
#
# print(b1 + 5)  # True(1) + 5 = 6
# print(int(b1))
#
# print(b2 + 5)  # False(1) + 5 = 5
# print(int(b2))

# print(bool("Python"))
# print(bool("")) # False
# print(bool(" "))
# print(bool(9))
# print(bool(0)) # False
# print(bool(False)) # False
# print(bool(None)) # False
#
# test = None
# print(test)
# test = 5
# print(test)

#  операторы сравнения.

# print(7 == 7)
# print(7 == 5)
# print(7 != 7)
# print(8 > 5)
# print(8 < 5)
# print(8 >= 8)
# print("привет" > "Привет")
# print("привет" < "Привет")
# print(2 < 4 < 9)  # True : True = True
# print(3 * 3 <= 7 >= 2)  # False &&  True = False
# print(2 * 5 > 7 >= 4 + 3)  # True && True = True

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

#  логические операторы

# print(5 - 3 == 2 and 1 + 3 == 4) # True and True = True
# print(5 - 3 == 2 and 1 + 3 < 4) # True and False = False

# print(5 - 3 == 2 or 1 + 3 == 4) # True or True = True
# print(5 - 3 == 2 or 1 + 3 < 4) # True or False = True

# print(not 9 - 5)
# print(not 9 - 9)
# a = 0
# print(not a)

# cnt = 15
# if cnt < 10:  # False
#     cnt += 1
#     print(cnt)


# age = int(input("Введите свой возраст : "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
# else:
#     print("Доступ запрещён")

# a = 15
# b = 5
# if a > b:
#     print("a>b")
# if b > a:
#     print("b>a")
# else:
#     print("b>a")


# a = input("Введите первую сторону: ")
# b = input("Введите вторую сторону: ")
# c = input("Введите третью сторону: ")
#
# if a == b == c:
#     print("Равносторонний")

# day = int(input("Введите день недели (цифрой) :"))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#         print("Рабочий день - ", end=" ")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
#
# elif day == 6 or day == 7:
#         print("Выходной день")
# else:
#         print("Такого дня недели не существует")


# a = int(input("Введите номер месяца : "))
# if a <= 1:
#     print("Лето")

#   от 0 до 9 включительно
#  ворона 1
#  вороны 2,3,4
#  ворон 5,6,7,8,9,0
#
# n = int(input("Введите количество ворон : "))
# if 0 <= n <= 9:
# print("На ветке ", end="")
# if n == 1:
#     print(n, " ворона ")
# if 2 <= n <= 4:
#     print(n, "вороны")
# if 5 <= n <= 9 or n == 0:
# print(n, "ворон")

# else:
# print("Ошибка ввода данных")


# 15.01.2023   занятие 4 Python. #
# j = 1
# i = 1
# while i < 5:
#     print("внешний цикл : i=", i)
#     j = 1
#     while j < 4:
#         print("\t внутренний цикл : j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#
#         j += 1
#         print()
#         i += 1


# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#         print()
#         i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# j = 0
# while j < 5:
#     print(" " * j, "*")
#     j += 1
# print()
# i = 0
# while i < 5:
#     j = 0
#     while j < i:  # 0 < 0
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:  # 0 < 0
#         print(end=" ")
#         j += 1
#     print("*")
#     i += 1

# for element in collection:
# ..... тело  цикла

# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'yellow', 'green':
#     print(color)


# print(range(9))
# range (start, stop, step)


# for i in range(2, 10, 1):
#     print(i, end=" ")
# print()
# i = 2
# while i <= 9:
#     print(i, end=" ")
#     i += 1

# a = int(input("введите целое число :"))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(11, 101, 11):
#     print(i, end=" ")
#     print()


# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done!')

# w = int(input("введите ширину прямоугольника :"))
# h = int(input("введите высоту прямоугольника :"))
# symbol = input("введите символ :")
# for i in range(h):
#     for j in range(w):
#         print(symbol, end="")
#     print()

# w = 16
# h = 4
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# w = [letter * 5 for letter in "hello"]
# print(w)
# num = [i for i in  range(30) if i % 2 == 0]
# print(num)


# списки (list)
# nums = [2, 5, 3, 7, 6,"H", 5, 1,True, 2, 6, 8, 9]
# print(nums)
# print(type(nums))


# nums = [8, 5, 3, 4, 1]
# print(nums)
# print(nums[1])
# print(nums[-1])
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(nums)
# print(len(nums))

# s = [5] * 6
# print(s)
# print(type(s))
#
#
# b = list("hello")
# print(b)
# print(type(b))
#
#
# c = s + b
# print(c)


# n = list(range(2, 10, 2))
# n2 = [2, 4, 6, 8]
# print(n)
# print(n2)
# if n == n2:
#     print("списки равны")
# else:
#     print("списки разные")


# генератор списков
# n = 5
# a = [i for i in range(1, n + 1)]
# print(a)
#
# c = [i * 3 for i in "list"]
# print(c)

# a = [0] * int(input("введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('-> '))
# print(a)

# a = [int(input("-> ")) for i in range(int(input(" n = ")))]
# print(a)
# a = [9, 8, 6, 4, 3]
# for i in range(len(a)):
#     print(i, ":", a[i])
#     print()
#
# for i in a:
#     print
#################################
#                               #
#   ЗАНЯТИЕ  5  Python ///      #
#     21.01.2023                #
#                               #
#################################

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# # for i in range(len(a)):
# #     if a[i] < 0:
# #         s += a[i]
# for i in a:
#     if i < 0:
#         s += i
#     print(s)

# n = list(range(21, 41))
# print(n)

# lst = [i for i in range(21, 41)]
# print(lst)
# a = 0
# b = 0
# for i in lst:
#     if i % 2 == 0:
#         a += 1
#     else:
#         b += i
#         print(f'Количество четных элементов списка: {a}\nСумма нечетных элементов: {b}')


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = k = 0
# for i in range(len(a)):
#     if a[i] != 0:
#         k += 1
#     s += a[i]
# print(s / k)

# a = [6, 3, 0, 8, 2]
# a[0],a[1] = a[1], a[0]
# print(a)

#  срез
#  список[start:stop:step]

# a = [6, 3, 0, 8, 2, 7]
# print(a[1:4])
# print(a[2:])
# print(a[:2])
# print(a[0:-1:1])
# print(a[0::1])
# print(a[::-1])
# print(a[4:0:-1])
# b = a[2:20]
# print(b)


# a = "hello"
# print(a[1:3])
#
# print(list(a))

# a = [6, 3, 0, 8, 2, 7]
# print(a[:])
# a[1:3] = [1, 1, 1, 1]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] =50
# print(a)
#
# b = 0
# del b
# print(b)

#  методы списка

# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a[5] = 99
# print(a)
# a.append(9)  # добавляет  один!   элемент в конец списка
# print(a)
# a.extend([5, 6, 7])
# print(a)
# a.extend("add")
# print(a)

# a = [6, 3, 0, 8, 2, 7]
# print(a)


# a = [6, 3, 0, 8, 2, 7]
# print(a)
# a.insert(2, 100)  # добавляет элемент списка (второй параметр- добавляемое значение
# # в определённое место  (первый параметр - задаёт индекс
# print(a)
# a.insert(0, 200)
# print(a)
#
# a.insert(len(a), 300)
# print(a)
#
# s = []
# n = int(input("кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("введите число"))
#     s.append(x)
# print(s)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):    x = int(input("Введите число кратное 3: "))
# if x % 3 == 0:        s.append(x)
# else:
#     print(x,"не делиться на 3 без остатка")
#     print(s)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i  in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)


# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55, ]
# c = []
# if len(b) > len(a):
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)


# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
# if len(a) > len(b):
#     a,b = b,a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# a.remove(1)  # удаляет первый по найденному совпадению
# # элемент из списка( по значению)
# print(a)
#
# last = a.pop()  # удаляет последний элемент из списка(без параметров)
# #  и возвращает удалённый элемент
#
# print(a)
# print(last)
# second = a.pop(-1)  #  удаление элемента по индексу
# print(a)
# print(second)
# a.clear() # очищает  список
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# k = int(input("введите индекс: 2\nk = "))
# a.pop(k)
# print(a)


# a = [5, 2, 9, 2, 1, 2, 4, 3, 2, 4]
# num = a.count(2) #  считает количество заданных значений в списке
# print(num)
#
# c = 2
# ind = a.index(2, 2) # возвращает положение первого индекса по заданному значению !
# print(ind)


# c = [1, 2, 3]
# d = c.copy()  #  возвращает копию  списка
# print("c =", c)
# print("d =", d)
# c.append(4)
# d.insert(0, 100)
# print("c =", c)
# print("d =", d)


# a = [5,4,6,7,8,9,7,5,4,33,4]
# a.reverse() #  перевернули элементы списков в обратном порядке
# print(a)
# a = [5, 4, 6, 7, 8, 9, 7, 5, 4, 33, 4]
# a.sort()  # отсортировали список по возрастанию
# print(a)

# a.sort(reverse=True)  # отсортировали список по убыванию
# print(a)

# a = [5, 4, 6, 7, 8, 9, 7, 5, 4, 33, 4]
#
# b = sorted(a, reverse=True)
# print("b =", b)
# print("a =", a)
#
# s = ["Виталий", "Сергей", "Александр", "Анна"]
# s.sort(key=len, reverse=True)
# print(s)


##############################################################
#                                                            #
# занятие 6  Python от 22,01,2023 Генерация случайных чисел   #
#                                                            #
##############################################################


# import random
#
#
# print(random.random())
# print(random.randint(0, 5))
# print(random.randrange(6, 15, 2))


# import random as r
#
# print(random.randint(0, 5))
# print(random.randrange(6, 15, 2))


# from random import randint, randrange as rr
#
# print(randint(0, 5))
# print(rr(6, 15, 2))


# from random import *
#
# print(randint(0, 5))
# print(randrange(6, 15, 2))
# print(round(uniform(10.5, 25.5), 2))
#
# city_list = ['Москва', 'Новосибирск', 'Воронеж ', 'Сочи', 'Екатеринбург']
# print(choice(city_list))
# print(choices(city_list, k=3))
#
# s = [55, 66, 77, 88, 99]
# print(choice(s))
# print(choices(s, k=3))
# shuffle(s)
# print(s)


# from random import randint
#
#
# mas = [randint(0, 20) for i in range(5)]
# print(mas)


#   функции агрегирования


# lst = [15, 8, 15, 11, 1]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))
#
# print("Hello" > "Hello")  # 72 < 104


# from random import randint
#
# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# max_1 = max(mas)
# print(max_1)
# print(max_1)
# mas.remove(max_1)
# mas.insert(0, max_1)
# print(mas)


# from random import randint
#
# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
#
# min_1 = min(lst)
# print(min_1)
#
# ind = lst.index(min_1)
#
# del lst[:ind]
# print(lst)
# print(lst[ind:])

# lst = []
# if len(lst) == 0:
#     print("список пустой")
#
# if not lst:
#     print("!!!список пустой")


# print(bool(lst))


# from random import randint

# n1 = int(input("введите размер первого списка: "))
# n2 = int(input("введите размер второго списка: "))
#
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for i in range(n2)]
# #
# print("первый список: ", a)
# print("второй список: ", b)
#
# c = a + b
# print("третий список", c)


# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#
# print("элементы обоих списков без повторений : ", c)


# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
#
# print("элементы общие для двух списков : ", c)
#
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)


# from random import randint
#
# k = int(input("размер списка: "))
# s = []
# while len(s) < k:
#     w = randint(0, k - 1)
#     if w not in s:
#         s.append(w)
# print(s)


# from random import randint

# m = [
#     [1, 2, 3, 4, ],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(len(m))
# print(m)
# print(m[1][2])


# a = [2, 'hello', 5]
# print(a[1][1])

# for row in range(len(m)):
#     print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()
# print()
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t\t")
#     print()
#
# for row in m:
# print(row)
# for x in row:
#     print(x**2, end="\t\t")
# print()


# from random import randint

# matrix = [[0 for x in range(5)] for y in range(3)]

# matrix = []
#
# for y in range(3):
#     new_row = []  # [[0,0,0,0,0]]
#     for x in range(5):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()


# for x, y in [[1, 2], [3, 4], [5, 6, ], [7, 8]]:
#     print(x, "+", y, "=", x + y)


# matrix = [[randint(1, 30) for x in range(5)] for y in range(3)]
# print(matrix)
# s = 0
# for row in matrix:
#     for j in row:
#         print(j, end="\t\t")
#     print()


# from random import randint
# n = int(input("n = "))
# m = [[randint(0, 100) for x in range(n)] for y in range(n)]
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()
# t = m[0][0]
# for k in range(n):
#     if t > m[k][k]:
#         t = m[k][k]
# print(t)

#  https //github.com /  зарегистрироваться . !!!!!!!!!

###########################################
#                                         #
#          28.01.2023 Занятие 7 .Python   #
#                                         #
###########################################

# print("hello")

# print("проверка репозитория")
#
# print("hello")


# ##########################################
#
#           Занятие 8. Python 29.01.2023
#
###########################################
# from math import pi
# 
# r = int(input ("Введите радиус окружности: "))
# s = round(2 * pi *r,2)
# print(s)


# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
# print(dir(time))


# s = time.time()
# print(s)
#
# local = time.ctime(s)
# print(local)
#
#
# res = time.localtime()
# print(res)
# print(res.tm_day, ".0", res.tm_mon, ".", res.tm_year, sep="")
#
# print(time.strftime("%d.%m.%Y"))
# print(time.strftime("Today is %B %d(%A), %Y."))
# print(time.strftime("Сегодня: %B %d(%A), %Y."))


# pause = 5
# print("программа запущена")
# time.sleep(pause)
# print("программа завершена")#text = input("название напоминания: ")

# start = time.time()
# time.sleep(5)

#    функции
# print()
#
#
# def hello():
#     print("Hello", name)
#
#
# hello("sergey")
# hello("Irina")


# def get_sum(a, b):
#     print("сумма: ")
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
#
# # get_sum('2', '5')
# print(res)

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#     else:
#         print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# print(int(input("Ведите число а :")))
# print(int(input("Ведите число b:")))
# def res(a,b):
#     if a>b:
#         return a-b
#     else:
#         return a+b
#     return "чиcла равны"
#
# print(res(a,b))

# def cub(a):
#     return a**3
#
#
# for i in range(1, 11):
#     print(i, "в кубе= ", cub(i))

# def change(lst):
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def func(x, y)
#     if x > y:
#         return True
#     else:
#         return False
#
#     print(func(10, 5))
#     print(func(10, 15))
#     a = 10
#     b = 15
#
#     if func(a, b):
#         print("gthвое число больше второго")
#     else:
#         print("второе число больше первого")

# def chek_password(password):
#     has_upper = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#
#     if len(password) >= 8 and has_upper:
#         return True
#     return False
#
#
# p = input("введите пароль: ")
# if chek_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")


# def get_sum(a=0, b=0, c=0, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# t = 2
# print(get_sum(1, 5, d=t))
# print("Результат", get_sum(2, d=1, a=5), sep="!!!!", end="\n\n")
# print(get_sum(1, 5, d=t))


# def display_info(name, age):
#     print("Name: ", name, "\nAge:", age, end="\n\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# #display_info("Igor", age=23, name="Ira")

#print("hello")

print("Проверка репозитория")