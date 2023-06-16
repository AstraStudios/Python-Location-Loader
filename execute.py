from random import choice
import random as random

print("This is a app for a random password")

digits = '1234567890'
chars = 'qwertyuiopasdfghjklzxcvbnm'
up = chars.upper()
special = '!@#$%^&*()-=_+[]\|;:<>,./?'

all = (str(digits + special) + chars + up)

password = ''.join(
    choice(all) for i in (10)
)

print(password)