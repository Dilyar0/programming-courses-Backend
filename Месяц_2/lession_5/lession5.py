from random import randint
import calculator
from person import Person
from termcolor import colored, cprint

man = Person("John", 27)
print(man)

cprint(man, "green", attrs=["underline"])