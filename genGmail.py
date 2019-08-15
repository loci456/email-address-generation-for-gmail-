
import random


gen = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
gmail = ['@gmail.com', '@googlemail.com']
target = input('Enter the email address before the "@" character' + "\n")
amount = input('set the required number of addresses ?'+ "\n")
length = input('set maximum generation length'+ "\n")
amount = int(amount)
length = int(length)
f = open("Gmail_generate.txt", "w")
for n in range(amount):
    salt =''
    for i in range(length):
        salt += random.choice(gen)
        f.write(target + "+" + salt + random.choice(gmail) + "\n")
        print(target + "+" + salt + random.choice(gmail))



