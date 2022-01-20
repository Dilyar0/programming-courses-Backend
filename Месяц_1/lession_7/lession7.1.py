from datetime import datetime
import time
from random import randint, sample, choice

letters = 'abcdefghijklmnopqrstuwxyz'
up_let = letters.upper()
numbers = '0123456789'
symbols = '!@#$%&*()'

secret = letters + up_let + numbers

password = sample(numbers, 6)
password = ''.join(password)
password += password.join(choice(letters))

password += password.join(choice(up_let))
print(password)

#
# print(secret)
#
# password = sample(secret, 8)



# a = ''.join(password)
#
# print(a)

# print(datetime.now())
# for i in 'Сейчас пройдет сколько-то секунд':
#     time.sleep(0.9)
#     print(i, end='')

