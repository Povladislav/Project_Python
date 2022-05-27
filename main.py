# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0
#
#     def __init__(self, x, y,z):
#         self.__x = x
#         self.__z = z
#         self.__y = y
#
#     def __getattribute__(self, item):
#         print("__getattribute__")
#         return object.__getattribute__(self, item)
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError("недопустимое имя атрибута")
#         print("__setattribute__")
#         object.__setattr__(self,key,value)
#
# pt1 = Point(100,23,1)
# print(pt1.MAX_COORD)
info = map(str,input().split())
list = list(info)
print(list)






