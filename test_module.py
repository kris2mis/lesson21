# # 1)
# import some_module
#
# b = some_module.B()
#
#
#
# # 2)
# from some_module import __a, __b, A, B
#
# a = A()
# # использование псевдонима
# from some_module import __a as alfa
#
# a = alfa
#

# 3) начинает работать all - инкапсуляция на уровне модуля

from some_module import *
from some_1 import *
from some_2 import *

test_a()

