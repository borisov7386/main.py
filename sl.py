# import sys, warnings
#
#
# if sys.version_info[0] < 3:
#     warnings.warn("Для выполнения этой программы необходима \
#                   как минимум версия Python 3.0")
# else:
#     print('Нормальное продолжение')
#

import os, platform, logging

p1 = ("wwww", "sfdsdsd")
p2 = ("gggg", "45455")
p3 = p1 + p2
print(*p3, sep="\n")
