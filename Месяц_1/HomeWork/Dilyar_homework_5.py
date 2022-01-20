# a)
#   Создать функцию которая принимает два аргумента - ширину и высоту прямоугольника.
# #   Функция должна возвращать площадь в виде числа с плавающей точкой.
def rectangle(width, height):
    print(width * height)

value1 = float(input("Enter the width: "))
value2 = float(input("Enter the height: "))

rectangle(value1,value2)

# b)
# Напишите функцию, которая принимает неограниченное количество чисел и возвращает их среднее арифметическое значение в виде целого числа.
def avarege(val, lst):
    for i in range(0, val):
        el = int(input("Enter the number: "))
        lst.append(el)
    avg = sum(a) / n
    print("meen value:",round(avg, 2))

n = int(input(" Enter the number of numbers: "))
a = []

avarege(n, a)

# c)
#    Напишите функцию "menu", которая принимает ключевые аргументы и возвращает словарь.
#    С помощью этой функции создать пару словарей с именованными аргументами как завтрак, обед, ужин.
def menu(**menus):
    return menus

menuOne = menu(breakfast="манты", lunch="Плов", dinner="яблоки")
menuTwo = menu(breakfast="каша", lunch="шаурма", dinner="апельсин")
print(menuOne)
print(menuTwo)
