name = "John"
age = 20

list_1 = ["python", 5, 3.9, True, name, age]

# [start:end:step] # отрезки
print(list_1[:2:3])

print(list_1[0]) # доступ по индексам
print(list_1[-1]) # самый последний элемент листа

list_3 = list_1[-1::-1]

# Методы листа
list_2 = [1,2,3,4,5]

list_2.append(6) # добавляет    
list_2.insert(1, 1.5) #добавляет эл. по выбору
list_2.extend(age) #удаляет по значению 
del list_2[3], list_2[4] #удаляет по индексу
list_2[2] = 3.0 #изменение объекта и замена
list_2.count(3)
list_2.clear() #удаляет всё
list_2.sort() #сортирует 
list_2.index(5) # 
list_2.remove(2) #удаляет по элементу
list_2.pop() #удаляет и хранит в себе значение элемента| ПРИМЕР:
                                                        # deleted = list_2.pop(0) 
print(list_2)

