# number = 125
# user_name = input("Как тебя зовут? ")
# running = True
#
# if user_name.casefold().__contains__("госпо"):
#     print("ну ты наглый конечно, буду звать тебя говно")
#     user_name = "говно"
#
# if user_name.casefold().__contains__("повел"):
#     print("ну ты наглый конечно, буду звать тебя говно")
#     user_name = "говно"
#
# print(f"{user_name}! Угадай число")
#
# while running:
#     user_input = int(input("Введи свой вариант : "))
#
#     if number == user_input:
#         print("Молодец, угадал \n:)")
#         running = False
#     if number > user_input:
#         print("Маловато \n :)")
#     if number < user_input:
#         print("Многовато \n :)")
# else:
#     print(f"Пока {user_name}, запусти меня ещё раз")
#
# for p1 in range(1,5):
#     print(p1)
# else:
#     print("всё")

# Тут про range ------------------------------

# for p1 in range(1,5):
#     print(p1)
# else:
#     print("всё")


# Тут про break ------------------------------

# while True:
#     p1 = input("Введите : ")
#     if p1 == "выход":
#         break
#     print("Длина строки:", len(p1))
# print("Вышли")

# Теперь тоже самое через break ----------------------------------

# number = 125
# user_name = input("Как тебя зовут? ")
# running = True
#
# if user_name.casefold().__contains__("госпо"):
#     print("ну ты наглый конечно, буду звать тебя говно")
#     user_name = "говно"
#
# if user_name.casefold().__contains__("повел"):
#     print("ну ты наглый конечно, буду звать тебя говно")
#     user_name = "говно"
#
# print(f"{user_name}! Угадай число")
#
# while True:
#     user_input = int(input("Введи число : "))
#
#     if number == user_input:
#         print("Молодец, угадал \n:)")
#         break
#     if number > user_input:
#         print("Маловато \n :)")
#     if number < user_input:
#         print("Многовато \n :)")
#
# print(f"Пока {user_name}, запусти меня ещё раз")

#  while True:
#      s = input('Введите что-нибудь : ')
#      if s == 'выход':
#          break
#      if len(s) < 3:
#          print("мало")
#      else:
#          print('Введённая строка достаточной длины')

# while True:
#     s = input('Введите что-нибудь : ')
#     if s == 'выход':
#         break
#     if len(s) < 3:
#         print("мало")
#         continue
#     print('Введённая строка достаточной длины')
# print('Выход')

# Тут про функции

# def hw():
#     print("Hello,world")
#
#
# hw()
# hw()
# hw()

# Работа с переменными

# def maxfunction1(a, b):
#     if a > b:
#         print(f"{a} больше {b}")
#     elif a == b:
#         print(f"{a} равно {b}")
#     else:
#         print(f"{a} меньше {b}")
#
#
# a = int(input("Введите первое число для сравнения : "))
# b = int(input("Введите второе число для сравнения : "))
#
# maxfunction1(a, b)

# Глобальная переменная

# a = int(input("Введите число для деления : "))
#
# def delenie():
#     global a
#     print("глобальная А", a)
#     a = a / 100
#     print("Поделённая А", a)
#
# delenie()
# print("Результат", a)

# Глобальные и НЕлокальные переменные

# y = 2
# print("Глобальный y =", y)
#
#
# def func_out():
#     global y
#     print(y)
#     x = y *10
#     print("x = y *10 =", x)
#     y = y + 777
#     print(y)
#
#     def func_in():
#         nonlocal x
#         print(x)
#         x = 210
#         print(x)
#
#     func_in()
#
#
# func_out()
#
# print(y)

# # Значения по умолчанию
# text = input("Введите значение ")
# times = int(input("Сколько раз повторить? "))
#
#
# def say(text, times = 10):
#     print(text * times)
#
#
# say(text, times)





