__author__ = "Khang Vinh Tran"

from hangman import *   # for using Hangman class
from random import *    # for using randint()

class Game:
    def __init__(self):
        """ 
        Initate a word bank for the object
        """
        self.bank = [ ] # Initiate the bank as an empty list
        self.theme = "" # Initiate the theme as an empty string
        # Looping until the player enter a valid theme
        while (self.theme != "animals" and self.theme != "clothes" and self.theme != "transportation" and self.theme != "veggies"):
            self.theme = input("The game will be launched after you choose 1 of these 4 themes: animals, clothes, transportation, or veggies: ")
        # read in the .txt file of the theme into the bank
        self.handle = open(self.theme + ".txt")
        for line in self.handle:
            line = line.rstrip()
            self.bank.append(line)
        # Close the handle after finish reading
        self.handle.close()
        #Create object t from Hangman class as an attribute for the class
        self.t = Hangman()        # create a Hangman object
        self.t.start()            # with the object self.t, cal the start() method to draw the scaffold
        seed()                  # Set seed for randint()
        


    def chooseWord(self):
        """
        Randomly pick out a word for the game
        """
        firstIndex = 0
        lastIndex = len(self.bank) - 1
        randIndex = randint(firstIndex, lastIndex)   #random a number of the first and the last index
        self.word = self.bank[randIndex]             #slice the bank to get the word
        # **** Strong notice: as long as there word has been created as a "self" variable of the class
        #  we don't have to return it and other methods of the class still recognize it.
        #return(self.word)

    def makeBoard(self):
        """
        Create a "__ " as the guess line for the game
        """
        self.guessBoard = [ ] 
        for letter in self.word:
            self.guessBoard.append("__")
        print(" ".join(self.guessBoard))   # Rather then using for loop and print( , end = "")
        print()                           

    def updateBoard(self):
        for i in range (0, len(self.word)):
            if self.word[i] == self.guess:
                self.guessBoard[i] = self.guess 
        print(" ".join(self.guessBoard))

            
    def playGame(self):
        """
        The body of the game.
        We allow players to guess to whlole word wight away, or:
        check if the single letter is in the word, or:
        check if that letter is not in the word
        """
        # **** Important: we have to call the method as self.method()
        self.chooseWord()     # Pick a word
        self.makeBoard()      # Create a guess line
        self.wrongCount = 0   # Initiate a counter for everytime player guesses wrong
        self.guessList = [ ]  # Initiate an empty list for the words that have been guessed
        
        while (self.wrongCount < 6 ):
            self.guess = input("Please guess a letter or the entire word: ")
            if (self.guess == self.word):
                break
            elif (self.guess in self.word):
                print("Correct! You have", str(6 - self.wrongCount), " attempts left")
                self.updateBoard()  # **** Calling method .updateBoard() to print the board
                if ("".join(self.guessBoard) == self.word):
                    break
            else:
                self.wrongCount += 1
                self.t.draw(self.wrongCount) # Calling method .draw() from class Hangman
                print("Wrong! You have", str(6 - self.wrongCount), " attempts left")
                print(" ".join(self.guessBoard))
            #append and print the letters which the player has guessed.    
            if not (self.guess in self.guessList):
                self.guessList.append(self.guess)
            print("You have guessed these following: ", self.guessList)
            print()
        # to determine Winning or Losing
        if (self.wrongCount < 6):
            print("GOOD JOB! YOU GET THE CORRECT WORD.")
        else:
            print("TOO BAD! YOU LOSE THE GAME. THE CORRECT WORD IS: " + self.word)
        
  
    def playLoop(self):
        repeat = "y"
        while (repeat == "y"):
            self.playGame() # **** Important: we have to call the method as self.method()
            repeat = input("Do you want to play again? (y/n) ")
            # To reset the graphic and starts the scaffold again.
            if (repeat == "y"):
                self.t.graphicReset()    #Call the graphicReset method we defined in class Hangman
                self.t.start()           # call the start method to draw the scaffold again.

    def __str__(self):
        return("The word bank is " +  str(self.bank) + " and the word choice is " + self.word)

    
g = Game()
g.playLoop()

