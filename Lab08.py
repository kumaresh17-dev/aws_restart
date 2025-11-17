import random
print("-------Guessing Game-------")
print("Guess number from 1 to 5")
number=random.randint(1,5)
isMatch=True
while isMatch!=False:
    guess=int(input("Enter the number : "))
    if guess==number:
        print("{} is the correct number".format(number))
        isMatch=False
    else:
        print("Try again...")
print("You win. Game is over")