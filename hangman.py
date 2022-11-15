import random
####################################################################################################
# this script only works for words with unique letters
# things to implement:
#   dont let the user guess the same thing twice
#   functionality for words with multiple of the same letter
#   only let the user enter a letter as the guess
####################################################################################################


# this function gets a random word
def getWord():
    words = ['ballsack']
    word = random.choice(words)
    return word

# this function creates a list of underscores (display for user)
def setup(word):
    guesslst=[]
    for letter in word:
        guesslst.append("_")
    return guesslst

# this function gets a guess from the user
def getguess():
    guess=input("enter your guess ")
    return guess

#this function plays hangman with the user
def hangman():
    randomword=getWord()
    print(randomword)
    randomwordlst = [letter for letter in randomword] # splitting word into a list
    print("get ready to play with Johns balls")
    display=setup(randomword)
    wrongletters = []
    wrongGuesses = 0
    while wrongGuesses < 7:
        print(" ".join(display)) # print display for user
        print("wrong guesses: " + ", ".join(wrongletters)) # print all wrong guesses so far
        guess=getguess()
        if guess in randomwordlst:
            guessIndex = randomwordlst.index(guess)
            display[guessIndex] = guess
            print("you guessed right! " + " ".join(display)) #prints display for user after correct guess
            if "_" not in display:
                print("you guessed right! the word was " + randomword)
                return
        else:
            print("that guess is wrong!")
            wrongletters.append(guess)
            wrongGuesses +=1

    return "You lost to johns balls"

hangman()
