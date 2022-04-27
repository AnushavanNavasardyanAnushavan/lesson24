# # N1
# class MinList:
#     def __init__(self, myList):
#         self.myList = myList

#     def mx(self):
#         self.myList.sort()
#         return self.myList[-1]
#     def mn(self):
#         self.myList.sort()
#         return self.myList[0]
    
#     def sm(self):
#         res = 0
#         for i in self.myList:
#             res += i
#         return res
# x = minList([0,5, 4, 1])
# print(x.mx())
# print(x.mn())
# print(x.sm())



# N2
# class MyDict:
#     def __init__(self, valueDict):
#         self.valueDict = valueDict

# class MaxValue(MyDict):
#     def __init__(self, valueDict):
#         super().__init__(valueDict)

#     def mV(self):
#         val = sorted(self.valueDict.values())
#         return val[-1]

# d = {1: 20, 2: 10, 3: 5}
# z = MaxValue(d)
# print(z.mV())



# N4
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width 

# x = Rectangle(5, 8)
# print(x.area())


# # 16֊սլայդի 6֊րդ խնդիրը
# class newDict:
#     def __init__(self, nDict):
#         self.nDict = nDict

#     def dictNew(self):
#         valueSort = sorted(self.nDict.values(), reverse=True)[:3]
#         keySort = sorted(self.nDict, reverse=True)[:3]
#         dictNeww = {}
#         for i, j in zip(keySort, valueSort):
#             dictNeww.setdefault(i, j)

#         return dictNeww

# a = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# x = newDict(a)
# print(x.dictNew())



# 18-սլայդի 7-րդ խնդիրը
# class SortDict:
#     def __init__(self, s):
#         self.s = s
#     def newDict(self):
#         a = self.s.split(",")
#         strliet = []
#         numliet = []
#         new_str_list = []
#         # new_num_list = []
#         # newdict = {}
#         for i in a:
#             if i.isdigit():
#                 numliet.append(i)
#             else:
#                 strliet.append(i)
#         # print(strliet)
#         # print(numliet)

#         for i in range(0, len(strliet) - 1):
#             if strliet.count(strliet[i]) > 1:
#                 new_str_list.append(i)
#         # print(new_str_list)

#         indexSum = 0
#         for i in range(0, len(numliet) - 1):
#             for j in new_str_list:
#                 if i == j:
#                     indexSum += int(numliet[i])
#         # print(indexSum)

#         for i in range(0, len(numliet) -1):
#             for j in new_str_list:
#                 if i == j:
#                     numliet[i] = indexSum

#         # print("numliet - ", numliet)

#         newDict1 = {}
#         for i, j in zip(strliet, numliet):
#             newDict1.setdefault(i, j)
#         print('newDict1 - ', newDict1)
# s = 'a,2,b,5,c,8,a,4,e,11'
# x = SortDict(s)
# x.newDict()


# # 21֊սլայդի 5-րդ խնդիրը
# class Sortinput:
#     def __init__(self, s):
#         self.s = s

#     def numSort(self):
#         numSum = 0
#         strSum = 0
#         for i in range(0, len(self.s)):
#             if self.s[i].isdigit():
#                 numSum += 1
#             else:
#                 strSum += 1
#         return f'numsum -  {numSum} strSum - {strSum}'
# a = "python3.9"
# x = Sortinput(a)
# print(x.numSort())


# # 30֊սլայդի 5-րդ խնդիրը
# class ListIndex:
#     def __init__(self, a):
#         self.a = a

#     def fanc(self):
#         user = int(input("Enter number --> "))
#         newList = []
#         for j in range(0, len(self.a)):
#             if user in self.a:
#                 print("True", self.a[j])
#                 break
#             else:
#                 for i in range(0, len(self.a)):
#                     res = user - self.a[i]
#                     if res  == 0:
#                         newList.append(res)
#                     elif res < 0:
#                         res *= -1
#                         newList.append(res)
#                     else:
#                         newList.append(res)
#                 print(newList.index(min(newList)))
#                 break
#                 # print(newList)

# a = [21, -9, 15, 2116, -71, 33]
# x = ListIndex(a)
# x.fanc()