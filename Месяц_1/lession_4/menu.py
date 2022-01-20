menu = {
    "lagman": {"тесто", "мясо", "перец"},
    "shashlyk": {"мясо", "лук", "помидор"}
}

for k, v in menu.items():
    quest = input("Введите ингридиент: ")
    if quest in v:
        print(k)
    else:
        print("Нет такого блюда! ")