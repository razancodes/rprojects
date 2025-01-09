#hangman game in python:
#hangman dict
import time 
import random
hangman={6:("-o->",
            "   ",
            "   "),
         5:(" o ",
            " | ",
            "   "),
         4:(" o ",
            "/| ",
            "   "),
         3:(" o ",
            "/|\\ ",
            "   "),
         2:(" o ",
            "/|\\",
            " ' "),
         1:(" o ",
            "/|\\",
            "/'  "),
         0:(" o ",
            "/|\\",
            "/'\\")}

def display(guessno):

    for item in hangman[guessno]:
        print(item)
def namelist1():
    namelist=["apple","journey","whisper","galaxy","puzzle","lantern","dream","river","echo","sunset","harmony","breeze",
    "shadow","canvas","melody","forest","stardust","adventure","serendipity","oasis","compass","mirage","twilight","phoenix","voyage"]
    return namelist
def guesser(str1):
    wrongguess=0
    list1=list(str1)
    dashlist=["-" for i in range(len(list1))]
    print(" ".join(dashlist))
    while wrongguess<7 :
        if dashlist==list1 and wrongguess<6:
            print(f"You Have guessed Correctly! The word is {str1}")
            prize=['bread omlet', 'mosambi juice', 'chikku juice', 'cone icecram', 'chocobar']
            print(f"You have won {random.choice(prize)}")

            break
        elif wrongguess>=6:
            print(f"You have killed hangman, the word was {str1}")
            break
        print("-"*14)
        print(f"The word is a {len(str1)} letter worda")
        display(wrongguess)
        print("-"*14)
        letterg=None
        print("time starts now: ")
        seconds=10
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end='\r')
            time.sleep(1)
            seconds -= 1
        letterg=input("Guess a Letter Now: ")
        if letterg in str1:
            for i in range(len(list1)):
                if list1[i]==letterg:
                    dashlist[i]=letterg
            print(" ".join(dashlist))
            print("-"*14)
            print()
        else: 
            wrongguess+=1
            print("-"*14)
            print("letter doesnt exist in the word")
            print(" ".join(dashlist))
guesser(random.choice(namelist1()))
