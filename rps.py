#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#

ROCK = "1"
SCISSOR = "2"
PAPER = "3"

print("Welcome to Rock, Paper, Scissors!")
print("Choose number from 1 to 3")
option = input("Choose number")
print("You have chosen" + option)
import random 

randint = str(random.randint(1,3))
print("Computer chosen" + randint)

if option == ROCK:
    if randint == PAPER:
        print("You lose")
    elif randint == SCISSOR:
        print("You won")   
    elif randint == ROCK:
        print("Draw")   
if option == SCISSOR:
    if randint == ROCK:
        print("You lose")
    elif randint == PAPER:
        print("You won")
    elif randint == SCISSOR:
        print("Draw")              
if option == PAPER:
    if randint == SCISSOR:
        print("You lose")
    elif randint == ROCK:
        print("You won") 
    elif randint == PAPER:
        print("Draw")               