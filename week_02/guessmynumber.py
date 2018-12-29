baseLow = 0
baseHigh = 100
numGuess = 50
print("Please think of a number between 0 and 100!")
while True:
    print("Is your secret number "+str(numGuess)+"?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if guess != "h" and guess != "l" and guess!= "c":
        print("Sorry, I did not understand your input.")
    elif guess == "l" and numGuess != 99:
        baseLow = numGuess
        numGuess = int((baseHigh+numGuess)/2)
    elif guess == "l" and numGuess == 99:
        numGuess = 100
        break
    elif guess == "h" and numGuess != 1:
        baseHigh = numGuess
        numGuess = int((baseLow+numGuess)/2)
    elif guess == "h" and numGuess ==1:
        numGuess = 0
        break
    else:
        break
print("Game over. Your secret number was: "+str(numGuess))
