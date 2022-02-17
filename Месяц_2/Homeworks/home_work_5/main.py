import os
import random
from envparse import env

class Casino:
    def __init__(self):
        self.cash = int(os.environ.get('MY_MONEY'))

        while int(self.cash) != 0:
            print(f"Ваши деньги: {self.cash}$")
            self.win_slot = random.randint(1, 30)
            self.slot = range(1, 31)
            self.bet = int(input('Сделайте ставку: '))

            if self.bet > self.cash:
                    print("У вас недостаточно денег")
            else:
                self.__choice = int(input('Выберите слот: '))
                if self.__choice > range:
                    print("Выберите слота только от 1-30")
                    repeat = input('Хотите ешё поиграть? ("да" или "нет"): ')
                    if repeat == 'да':
                        continue
                    elif repeat == "нет":
                        break
                    else:
                        continue
                        print('"да" или "нет"?')

                if self.win_slot == self.__choice:
                    self.cash += self.bet
                    print(f'You win\n money: {self.cash}')
                    if self.win_slot == self.__choice:
                        ans = input('do you want to play more?(yes or write any words): ')
                        if ans != 'yes':
                            break

                else:
                    self.cash -= self.bet
                    print(f' You lost \n money: {self.cash}')
                    if self.win_slot != self.choice:
                        ans = input('do you want to play again?(yes or write any words): ')
                        if ans != 'yes':
                            break




env.read_envfile('settings.env')