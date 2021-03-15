# try:
#     text = input('Введите что-нибудь --> ')
# except EOFError:
#     print('Ну зачем вы сделали мне EOF?')
# except KeyboardInterrupt:
#     print('Вы отменили операцию.')
# else:
#     print('Вы ввели {0}'.format(text))


class ShortInputException(Exception):
    """User exception class"""
    def __init__(self, len, atleast):
        Exception.__init__(self)
        self.len = len
        self.atleast = atleast


try:
    text = input('Введите что-нибудь --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print(f"Длина введенной строки {ex.len}, ожидалось не менее {ex.atleast}")
else:
    print('Не было исключений.')


131