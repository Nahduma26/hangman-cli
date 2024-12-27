import requests
import json
import random
URL='https://random-word-api.herokuapp.com/word?number='

def getWords(num):
    response=requests.get(URL+str(num)).text
    return json.loads(response)

a = getWords(1000)

randomWord = random.choice(a)
blankWord = ['_'] * len(randomWord)
guessesAvailable = 7
def main():
    while guessesAvailable > 0:
        guess = input("Please enter your guess \n")
        playHangman(guess)

def playHangman(guessProvided):
    for i in range(0, len(blankWord)):
        print(blankWord[i], sep='')
    if (not guessProvided.isAlpha()):
        print("Invalid guess. Try again")
        return
    if (not randomWord.lower().contains(guessProvided)):
        print("Incorrect guess. You have " + guessesAvailable + " guesses left.")
        guessesAvailable -= 1
    else:
        for i in range(0, len(randomWord)):
            if randomWord[i] == guessProvided:
                blankWord[i] = guessProvided
        print("Updated word: \n")
        for i in range(0, len(blankWord)):
            print(blankWord[i], sep='')