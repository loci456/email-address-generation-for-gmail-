import random
from itertools import product


gmail = ['@gmail.com', '@googlemail.com']
gen = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def dot():
    f = open("Gmail_generate.txt", "w")
    target = input('Enter the email address before the "@" character:\n' + "[mail]--->")
    for prod in product((".", ""), repeat=len(target) - 1):
        mixed = [char for tpl in zip(target, prod + ("",)) for char in tpl]
        new_word = "".join(mixed)
        f.write(new_word + random.choice(gmail) + '\n')
        print(new_word)

def across():
    f = open("Gmail_generate.txt", "w")
    target = input('Enter the email address before the "@" character:\n' + "[mail]--->")
    amount = input('set the required number of addresses ?:\n' + "[value]--->")
    length = input('set maximum generation length:\n' + "[value]--->")
    amount = int(amount)
    length = int(length)
    for n in range(amount):
        salt = ''
        for i in range(length):
            salt += random.choice(gen)
            f.write(target + "+" + salt + random.choice(gmail) + "\n")
            print(target + "+" + salt + random.choice(gmail))

def together():
    f = open("Gmail_generate.txt", "w")
    target = input('Enter the email address before the "@" character:\n' + "[mail]--->")
    amount = input('set the required number of addresses ?:\n' + "[value]--->")
    length = input('set maximum generation length:\n' + "[value]--->")
    amount = int(amount)
    length = int(length)
    for prod in product((".", ""), repeat=len(target) - 1):
        mixed = [char for tpl in zip(target, prod + ("",)) for char in tpl]
        new_word = "".join(mixed)
        print(new_word)
        for n in range(amount):
            salt = ''
            for i in range(length):
                salt += random.choice(gen)
                f.write(new_word + '+' + salt + random.choice(gmail) + '\n')
                print(new_word + "+" + salt + random.choice(gmail))






while True:
    q = input('Select the desired option:\n'
          '1. With a dot.\n'
          '2. With the addition at the end.\n'
          '3. Combined variant\n'
          '[Select]--->')

    if q == '1':
        dot()
    elif q == '2':
        across()
    elif q == '3':
        together()
