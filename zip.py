# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
# 2. Резервные копии должны храниться в основном каталоге резерва.
# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
# 5. Будем использовать стандартную команду zip, имеющуюся по умолчанию в любом
# стандартном дистрибутиве GNU/Linux. Пользователи Windows могут установить её
# со страницы проекта GnuWin32 и добавить «C:\Program Files\GnuWin32\bin» к
# системной переменной окружения PATH, аналогично тому, как мы это делали для
# самой команды «python». Обратите внимание, что для этого подойдёт любая команда архивации,
# если у неё есть интерфейс командной строки, чтобы ей можно было
# передавать аргументы из нашего сценария

import os
import time

source_dir = ["/home/zuxel/copy"]
files = os.listdir(source_dir[0])
print(files)

# target_dir = "/home/zuxel/back"
#
# target_name = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
#
# zip_command = "zip -r {0} {1}".format(target_name, " ".join(source_dir))
#
# print(zip_command)
#
# if os.system(zip_command) == 0:
#     print("Done, лежит в", target_name)
# else:
#     print("Что то пошло не так, чувак")