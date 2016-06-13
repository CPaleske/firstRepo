#Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 12:49:54)
#[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
#Type "copyright", "credits" or "license()" for more information.
#!/usr/bin/python

#How to play this game:
#1. import guessnum_game as a module in terminal window.
#2. input guessnum_game.thegame() to play!


#Importing modules:
import random
from random import randint

#Global variables:
target = randint(1,50)
num_guess = 5

#Functions:
def welcome():
    print "Hi there. What is your name?:"
    name = raw_input()
    print "Hello " + name + ". I'm thinking of a number between 1 and 50."
    print "You have 5 guesses."

def guess():
    for n in range(num_guess):
        usr_guess=int(input("Guess a number: "))
        if usr_guess > target:
            print "Too high!"
        elif usr_guess < target:
            print "Too low..."
        else:
            print "You guessed the number!"
            break
    if usr_guess != target:
        print "You didn't guess the number in time...the number was:"
        print target

def thegame():
    welcome()
    guess()


