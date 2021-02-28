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

# Версия 1
# import os
# import time
#
# source_dir = ["/home/zuxel/copy"]
# files = os.listdir(source_dir[0])
# print(files)
#
# target_dir = "/home/zuxel/back"
#
# target_name = target_dir + os.sep + time.strftime('%Y-%m-%d-%H%M%S') + '.zip'
#
# zip_command = "zip -r {0} {1}".format(target_name, " ".join(source_dir))
#
# if os.system(zip_command) == 0:
#     print("Done, лежит в", target_name)
# else:
#     print("Что то пошло не так, чувак")
#
# # Версия 2
# import os
# import time
#
# # Откуда копируем
# source_dir = ["/home/zuxel/copy"]
# # Куда копируем
# target_dir = "/home/zuxel/back"
# # Если папки назначения не существует, создаём
# if not os.path.exists(target_dir):
#     os.mkdir(target_dir)
#     print("Папка назначения создана")
# else:
#     print("Папка назначения сущестует")
# # Имя папки = дата архивации
# folder_name = target_dir + os.sep + time.strftime("%Y%m%d")
# # Имя файла с архивом
# file_name = time.strftime("%H%M%S")
# # Создаём папку внутри папки назначения, если ее ещё нет
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
#     print("Папка создана")
# else:
#     print("Папка для текущей даты уже есть, новую не создаём")
# # Собираем имя файла назначения из имени папки, разделителя, имени файла и расширения .zip
# target_name = folder_name + os.sep + file_name + '.zip'
# # Собираем zip команду
# zip_command = "zip -r {0} {1}".format(target_name, " ".join(source_dir))
# # Выполняем арживацию
# if os.system(zip_command) == 0:
#     print("Done, лежит в", target_name)
# else:
#      print("Что то пошло не так, чувак")

# Версия 3
# Подключаем модули
import os
import time
# Откуда копируем
source_dir = ["/home/zuxel/copy"]
# Куда копируем
target_dir = "/home/zuxel/back"
# Если папки назначения не существует, создаём
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print("Папка назначения создана")
else:
    print("Папка назначения сущестует")
# Имя папки = дата архивации
folder_name = target_dir + os.sep + time.strftime("%Y%m%d")
# ВВод комментария к архиву
comment = input("Введите комментарий к архиву здесь ->")
if len(comment) == 0:
    # Имя файла с архивом без комментария
    file_name = time.strftime("%H%M%S")
else:
    # Имя файла с архивом + комментарий. Если в комментарии есть проблемы, заменяем их на _
    file_name = time.strftime("%H%M%S") + "_" + comment.replace(" ", "_")
print(file_name)

# Создаём папку внутри папки назначения, если ее ещё нет
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("Папка создана")
else:
    print("Папка для текущей даты уже есть, новую не создаём")
# Собираем имя файла назначения из имени папки, разделителя, имени файла и расширения .zip
target_name = folder_name + os.sep + file_name + '.zip'
# Собираем zip команду
zip_command = "zip -r {0} {1}".format(target_name, " ".join(source_dir))
# Выполняем арживацию
if os.system(zip_command) == 0:
    print("Done, лежит в", target_name)
else:
     print("Что то пошло не так, чувак")