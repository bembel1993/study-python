a = [1,2,3]
b = a.append(4) # append() добавляет элемент
c = a.pop() # pop() удаляет
print(a, b, c)

# Индексы
b = {"name": "Vitali", 1: 2}
print(b["name"], b[1])

# Записать фамилию в словарь. К массиву b присваиваем новое ключ-значение
b["surname"] = "Bembel"

# Удалить ключ-значение
#del b["name"]
print(b)


a = ["asd", 1, 1.0, 4, {1,2,3}]
a[4] = 5
del a[1]
print(a)

a = [1, 2, 3, 4]
c = a.copy()
b = a.pop(2)
print(a, b, c)

a = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4]
c = a.copy()
b = a.pop(2)
print(a.count(1)) #выводит количество одинаковых объектов в массиве//
#a.clear()
#a.extend((1, 2, 3)) #добавляет в конец массива "а" объекты
print(a, b, c)

a = [1, 2, 3, 4]
print(a.index(3)) #выводит индекс элемента в массиве, здесь значение 3 имеет индекс 2

a = [1, 10, 6, 9, 200, 153]
a.sort()
print(a)

# == - оператор сравнения
# != - не равно
a = 5
b = 5
print (a == b)
print (a != b)
print (a>b)

# and or not
# and - возвращает последний true или false
a = 5 and 6
print(a)

# git команды:
# git branch - список веток
# git log - посмотреть все коммиты в ветке
# git checkout -b "name_branch" - создать новую ветку и переключиться на нее
# git switch main (itacademy)- переключиться на ветку
# git merge itacademy (main) - слияние коммитов главной ветки со второстепенной, после переключения на ветку main