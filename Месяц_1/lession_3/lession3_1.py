words = tuple(["python", "int", "list", "turples", "str"])
new = []

for i in words:
    if len(i) <= 3:
            new.append(i.upper())
print(new)

#-------------------------------------------------------------------------------------------------

while 1:
    word = input("Вводите что угодно")
    number = 0
    letter = 0
    for i in word:
        if i.isnumeric():
            number += 1
        else:
            letter += 1
    print(
        f"{word}",
        f"Объектов в слове: {len(word)}\n",
        f"Числа: {number}\n",
        f"Буквы: {letter}"
    )