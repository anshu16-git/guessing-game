import random
import math
x = random.randint(1,100)
print("\n\tYou have only ", round(math.log(100 - 1 )), "chances to guess the integer!\n")
#Initializing the no of guesses.
count = 0
while count < math.log(100 - 1 ):
    count += 1
    guess = int(input("Guess A Number: "))
    if x == guess:
        print("Congratulation you did it in ",count, "try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")
if count >= math.log(100 - 1 ):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
