#=================================== модули
from lesson_5 import greeting as g
from random import randint
from datetime import datetime

c = 0
cash = 500
start = datetime.now()
while cash != 0:
    c += 1
    bet = int(input(f'Введите ставку: (Доступно: {cash})'))
    if bet > cash:
        print(f'Сумма не должна превышать {cash}')
        continue
    comp = randint(1, 3), randint(1, 3)
    user = randint(4, 6), randint(4, 6)

    if c == 5:
        comp = randint(4, 6), randint(4, 6)
        user = randint(1, 3), randint(1, 3)

    if sum(comp) > sum(user):
        print('You lost')
        cash -= bet
    elif sum(comp) < sum(user):
        if c == 4:
            print('Ты сорвал джек-пот')
            cash += (bet * 2)
        else:
            print('You win')
            cash += bet

    else:
        print('Draw!')

    print(comp, 'comp')
    print(user, 'user')
end = datetime.now()
print(f'Времени потрачено {end - start}')

# numbers = ['a', 'b', 'c', 'd', 'e']
# print(random.choice(numbers))
#
# print(random.sample(numbers, 2))
#
# print(randint(1, 5))

