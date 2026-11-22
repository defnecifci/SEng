import random

secret_num = random.randint(1,100)
guess = 0

while True
    guess = int(input("Try to guess: "))
    if guess < secret_num:
        print("Too small")
    elif guess > secret_num:
        print("Too big")
    else

print(secret_num)