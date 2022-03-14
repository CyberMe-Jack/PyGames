#!/bin/env python3

import random


#Hangman
def hangman(word):
    gamecontinue = True
    #Count how many letters in word
    lettercount = 0
    for letter in word.rstrip():
        lettercount+=1
    print(f"The word has {lettercount} letters, good luck!")

    #Take letters from word turn into list
    answer = []
    for letter in word:
        answer.append(letter)
    answer.pop()   #Delete \n
    #Define guess list based on answer using _
    guessanswer = []
    for letter in answer:
        guessanswer.append("_")
    #Run game
    attempts = 5
    while gamecontinue:
        guess = input(f"{attempts} attempts to guess the right answer remain\n:")
        listposition = 0        #Used in for loop to place matching letter in correct spot
        for letter in answer:
            if guess == letter:
                guessanswer[listposition]=(guess)
            listposition+=1
        print(guessanswer)
        #Check answer each iteration
        if guessanswer == answer:
            print(f"Correct! {word.rstrip()} was the answer.")
            gamecontinue = False

        attempts-=1
        #Game over
        if attempts==0:
            print("You suck!")
            gamecontinue = False
    return


#Get word from list
def getword():
    """Open and read from file"""
    # File
    filepath = './wordlist.txt'
    services = open(filepath,'r')
    # Read file /Store list
    wordlist = services.readlines()
    # Choose random word to return
    totalwords = 0
    for line in wordlist:
        totalwords+=1
    randomnum = random.randint(0,totalwords-1)
    randomword = wordlist[randomnum]
        
    return randomword

#Add a word to list
def newword():
    """Open and append wordlist"""
    # File
    filepath = './wordlist.txt'
    services = open(filepath,'a')
    customword = input("Enter word: ")
    services.write(f"{customword}\n")
    services.close()

#Menu function
def menu(choice): 
    if choice=="1":
        #Start game function
        getword()             # Get word from wordlist.txt
        hangman(getword())    # Start game, pass random word through
    elif choice=="2":
        #Add word function
        newword()
    return

#Get menu choice
print("Welcome, please select from the following choices")
menuon = True
while menuon:
    choice = input("1.New Game\n2.Add word\n3.Quit\n:")
    #Select menu choice
    menu(choice)
    #Quit game
    if choice=="3":
        print("GoodBye")
        menuon = False
