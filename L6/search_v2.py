import random

number = random.randint(1, 101)
count = 0


up = 100
low = 0
while True:
    if (up+low)/2 == number:
        print("Computer's number is", number)
        print("You have", count, "tries")
        break
    elif (up+low)/2 > number:
        up = int((up+low)/2)
    elif (up+low)/2 < number:
        low = int((up+low)/2)
    count += 1
