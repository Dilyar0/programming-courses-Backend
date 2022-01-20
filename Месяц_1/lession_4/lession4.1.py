# ===============================   set
lagman = {"тесто", "мясо", "перец"}
shashlyk = {"мясо", "лук", "помидор"}

# из двух setov он вернёт только общие
print(lagman.intersection(shashlyk))  
print(lagman & shashlyk)  # укороченная версия

# объединение нескольких множеств.
print(lagman.union(shashlyk)) 
print(lagman | shashlyk) # укороченная версия

# множество из всех элементов set, не принадлежащие ни одному из other.
print(lagman.difference(shashlyk))
print(lagman - shashlyk) # укороченная версия

# множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
print(lagman.symmetric_difference(shashlyk))
print(lagman ^ shashlyk)

lagman.add() #добавляет что-то
lagman.remove() #удаляет что-то
lagman.clear() # очистка множества.

# -----------------------------------------------------------------------------------------------------
students = []
abituriends = [
    dict(name="Azamat", ORT="110"),
    dict(name="Bektur", ORT="90"),
    dict(name="Azamat", ORT="150"),
]
while 1:
    for i in abituriends:
        if i["ORT"] >= 110:
            students.append(i)
        else:
            print(f"{i} не проходить! ")
            
print(students)