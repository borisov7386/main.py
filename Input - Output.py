import re


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


try:
    something = (input("Введите текст: ")).lower()
except EOFError:
    print("Ну спасибо за EOF")
except KeyboardInterrupt:
    print("\nОтмена")
else:
    something = re.sub(r'[\W]', '', something)
    # print(something)
    if is_palindrome(something):
        print("Да, это палиндром")
    else:
        print("Нет, это не палиндром")

# 128