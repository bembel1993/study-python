# names = ["John", "Alex", "Kate", "Nikol"]
#
# количество итераций является длинной объекта == len(obj)
#
# for name in names:
#     print(name)


# fruits = {"apple": 10, "banana": 20, "peach": 30}
# print(fruits.values())
# for fruit in fruits.values():
#     print(fruit)
#
# for fruit in fruits:
#     print(fruit)


# fruits = {"apple": 10, "banana": 20, "peach": 30}
# for fruit in fruits:
#     print(fruit, fruits[fruit])
#
# keys_and_value = fruits.items() # ('apple', 10) - кортеж
# print(keys_and_value)
# for fruit, price in fruits.items():
#     print(fruit, price)


# range функция, которая принимает в себя три аргумента (start, stop, step) stop(бязательный), start = 0, stop = 1
# выводит диапазон значений
# a = list(range(10)) # start
# print(a)
# a = list(range(2, 10)) # start, stop
# print(a)
# a = list(range(2, 10, 2)) # start, stop, step
# print(a)
# for i in range(2, 10, 2):
#     print(i)


# enumerate - возвр. список кортежей (индекс, значение)
# a = ("asd", "asdd", "asddd", "asdddddd")
# enum = list(enumerate(a))
# print(enum)
# for index, value in enumerate(a):
#     print(index, value)
# for index, value in enumerate(a):
#     print(a[index])


# for x in range(1, 11):
#     print(x)
# else:
#     print("End")


# a = ("asd", "asdd", "asddd", "asdddddd")
# for i in a:
#     if isinstance(i, (int, float)):
#         print(i + 10)
#     if isinstance(i, str):
#         print(i)
#     else:
#         break

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = []
#
# for i in a:
#     #print(i)
#     if i % 2 == 0:
#         b.append(i)
#
# print(b)


# a = [3, 6, 4, 9]
# target = 7
# b = []
# c = []
# for index, velue in enumerate(a):
#     #print(velue)
#     for index2, velue2 in enumerate(a):
#         b = velue2 + velue
#         if b == target:
#             c.append(index)
#             print(velue2)
# print(c)


# num = 100
# num2 = int(input("Угадай число"))
# while num2 <= num or num2 >= num:
#     if num2 == num:
#         print("Число верно: ", num)
#         break
#     if num2 != num:
#         num2 = int(input("Угадай число"))
#         continue


# a = [i for i in range(10)]
# print(a)

# b = [1, 2, 3, 4, 5]
# a = [1 for i in b if i % 2 == 0]
# print(a)

# a = {k: v + 1 for k, v in enumerate(range(10))}
# print(a)

# a = {v for v in range(10) if v <= 3}
# print(a)

# a = list(range(100))
# b = {c for c in a if c % 3 == 0 and c % 5 == 0}
# print(b)

a = ["Kirill" + f" {i}" for i in range(5)]
print(a)