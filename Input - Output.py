import re


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = (input("Введите текст: ")).lower()
# print(something)
something = re.sub(r'[\W]','', something)
# print(something)

if is_palindrome(something):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
