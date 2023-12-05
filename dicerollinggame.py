'''
Write a program that simulates a dice game where the player rolls two dice and
calculates the sum of their values. If the sum is 7 or 11, print "You win!" 
If the sum is 2, 3, or 12, print "You lose!" Otherwise, print "Roll again."

'''
from random import randint

while True:
    roll =input('Roll Y or N')
    if roll.lower() == 'y':
        a = randint(1,6)
        b = randint(1,6)
        
        if a + b == 7 or a + b == 11:

            