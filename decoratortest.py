


# #вызов 1 функции через другую
# def decorator(func):
#     if type(func).__name__ == "function":
#         func()
#
#
# decorator(testing)
#
# print(type(testing).__name__)  #function


# #вызов функции через параметр
# def decorator():
#     def wrapper():
#         print("testinf wrapper function...")
#
#     return wrapper()
#
#
# t = decorator()
# t()


def decorator(func):
    def wrapper():
        print("Before starting...")
        func()
        print("After starting")  # но саму функцию wrapper не вызывали

    return wrapper


@decorator
@decorator
def testing():
    print("testing....")


# f = decorator(testing)  # название, а не функцию  f = decorator(testing())
# f()


#название f можно поменять - это декорация
# testing = decorator(testing)
# testing = decorator(testing)
# testing = decorator(testing)
testing()

# вместо 3 действий - аннотация (см. выше)

