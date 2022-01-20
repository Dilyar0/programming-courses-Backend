from random import randint
from datetime import datetime

count = 0
secret = randint(0, 100)
start = datetime.now()
while True:
    count += 1
    try:
        number = int(input('Введите число: '))
    except:
        print('Вводи только числа')
        continue

    if number > 100:
        print("Введите меньше 100!!!")
    if number < 0:
        print("Введите больше 0!!!")
    if number > secret:
        print("<")
    elif number < secret:
        print(">")
    else:
        print(f"Вы угадали🎉 - {secret}")
        break
    if number <= secret + 5 and number >= secret - 5:
        if number < secret:
            print("очень близко")
        else:
            print("очень близко")
    elif number <= secret + 10 and number >= secret - 10:
        if number < secret:
            print("близко")
        else:
            print("близко")
end = datetime.now()


print(f'{end - start} - Всего времени')
print(f"{count} - Попытки")