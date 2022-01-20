# 1) Дан словарь состоящий из основных данных нашего учебного заведения:
GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

# Удалить bag
del GeekTech['bag']

# Изменить адрес на нынешний
GeekTech['address'] = "Ibraimova 103"

# Добавить номер телефона и инстаграмм аккаунт Гиктека
GeekTech["contacts"] = "+996-507-052-018"
GeekTech["instagram"] = "geektech__kg"

# Добавить/расширить список актуальными курсами, которые вы знаете. Затем преобразовать этот список в кортеж
GeekTech['courses'].append("iOS")
GeekTech['courses'].append("IT English")
GeekTech['courses'].append("UX/UI")
GeekTech['courses'].append("GeekCamp")

GeekTech['courses'] = tuple(GeekTech['courses'])

# Вывести словарь на экран с помощью цикла for с получением всех пар 
# “ключ: значение”
for k, v in GeekTech.items():
    print(f"{k}: {v}")
    
print(GeekTech.keys())
print(GeekTech.values())