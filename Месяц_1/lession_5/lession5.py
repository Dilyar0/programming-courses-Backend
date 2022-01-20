# =====================функции
from socket import if_indextoname


def greeting(name):
    print(f"hello, {name}")
greeting("max")
greeting("anna")

# return in function
def plus(a,b):
    return a + b 
plus(5,2) 

# greeteng

def greeteng(name):
    print("Hello, ",name)


students = [
    {"name":"Aman","h_w":5, "deadline":True,"points":39, "last_rate":10},
    {"name":"Dilyar","h_w":5, "deadline":True,"points":39, "last_rate":10},
    {"name":"Amantur","h_w":5, "deadline":False,"points":39, "last_rate":10},
    {"name":"Atabek","h_w":5, "deadline":False,"points":39, "last_rate":10},
]
#функция проверки домашки у студента
def checker():
    for i in students:
        if i["deadline"] == False:
            i["last_rate"] = 10
            i["points"] += i["last_rate"]
        else:
            i["last_rate"] = 5
            i["points"] += i["last_rate"]
    for i in students:
        print(i)
#функция проверки студенда
checker()
def delete(name):
    for i in students:
        if name in i.values():
            students.remove(i)
delete("Aman")

#фукция переименования студенда
def find_student(name):
    for i in students:
        if name in i.value():
            return i

def edit(name,new_name):
    if find_student(name):
        print(students.index(find_student(name)))
        students[students.index(find_student(name))]["name"] = new_name
    else:
        print("no student")
edit("Atabek","Amanbek")

# ===============типы аргументов в функции=====================================================

# позиционные аргументы
def calc(*args):
    return args
print(calc(5,3,2,5))

# ключевые аргументы
def calc2(a,b=2):
    print(calc2(1, ))

# именованные аргументы
def car(**kwargs):
    return kwargs
print(car(mark="bmw", model="e34", color="black"))

# ==========практика====================================================================
students = [
    {"name": "Aman", "standup": 2 }
]
