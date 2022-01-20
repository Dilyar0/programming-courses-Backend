from ast import Num
from cgi import print_directory
from cmath import inf


list1 = ["python","exceptions","lamda"]
list2 = ["functions","arguments","keyword arguments"]  

def up_letter(word: str):
    return word.capitalize()


def edit(words,func):
    for word in words:
        print(func(word))

edit(list1,up_letter)
edit(list2,up_letter)

# ============= lambda =============================================================================

def square(number):
    return number ** 2
print(square(5))

# это одно тоже/ это чудо называется lambda
square_1 = lambda number: number ** 2

print(square_1(5))

a = lambda x, y,: x + y
print(a(3,4))
# ---------------------------------------------------------------------------------------------

nominal = ["Т.Молдо","К. Датка", "Т.Сатылганов","А.Осмонов","С.Каралаев"]
number = [20,50,100,200,500]
info = dict(zip(number,nominal))
print(info)


# c = 0
# while c != len(nominal):
#     info = dict(number=number[c], nominal=nominal[0])
#     c += 1
# print(info)

squareT = list(map(lambda x: x * x, number))
print(squareT)

filter = list(filter(lambda x: x > 100,number))