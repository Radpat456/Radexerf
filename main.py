import random
fakty = []
for i in range(3):
    fakty = []
    a = input("jakie są fakty o tobie?")
    fakty.append(a)
print(random.choice(fakty))
