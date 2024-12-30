import requests
import json
import random
import sys
URL='https://random-word-api.herokuapp.com/word?number='

def resetGame():
    global randomWord, blankWord, guessesAvailable, guessedLetters
    a = getWords(1000)
    guessedLetters = []
    randomWord = random.choice(a)
    blankWord = ['_'] * len(randomWord)
    guessesAvailable = 7

def getWords(num):
    response=requests.get(URL+str(num)).text
    return json.loads(response)

def main():
    resetGame()
    while guessesAvailable > 0:
        guess = input("Please enter your guess \n")
        playHangman(guess)
        if "_" not in blankWord:
            print("You have won the game!")
            choice = input("Do you want to play again? Type 'yes' or 'no'.")
            while (choice.lower() != "yes" and choice.lower() != "no"):
                choice = input("Do you want to play again? Type 'yes' or 'no'.")
            if choice.lower().strip() == "yes":
                resetGame()
            else:
                sys.exit()
    print("Game over, you have lost. The word was " + randomWord)
            

def playHangman(guessProvided):
    global guessesAvailable
    global blankWord
    blankWordString = "".join(blankWord)
    print(blankWordString)
    if (not guessProvided.isalpha() or len(guessProvided) > 1 or guessProvided in guessedLetters):
        print("Invalid guess. Try again")
        return
    if (guessProvided not in randomWord.lower()):
        guessesAvailable -= 1
        print("Incorrect guess. You have " + str(guessesAvailable) + " guesses left.")
    else:
        for i in range(0, len(randomWord)):
            if randomWord[i] == guessProvided:
                blankWord[i] = guessProvided
        print("Updated word: \n")
        updatedWord = "".join(blankWord)
        print(updatedWord + "\n")
    guessedLetters.append(guessProvided)

if __name__ == "__main__":
    main()
    