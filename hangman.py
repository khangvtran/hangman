__author__ = "Khang Vinh Tran"

from turtle import *

class Hangman:
    """
    class Hangman
    Draw the scaffold
    Draw the body
    """
    def __init__(self):
        self.t = Turtle()  # Create object Turle() as an attribute
        self.t.speed(0)    # Speed up the object for testing purpose
    def start(self):
        """
        method start() simply is to draw the scaffold
        """
        # hide the object cursor
        self.t.ht()        
        # get in a position for the scaffold
        self.t.up()
        self.t.goto(-120, -120)
        self.t.down()
        # draw the scaffold
        self.t.pensize(6)
        self.t.forward(260)
        self.t.back(130)
        self.t.left(90)
        self.t.forward(300)
        self.t.right(90)
        self.t.forward(130)
        # draw the rope
        self.t.pensize(3)
        self.t.right(90)
        self.t.forward(40)

    def draw(self, wrongCount):
        """
        method draw() uses the self.t attribute
        It takes in an int value of the number of wrong guess the player has made
        Draw the part of the hangman body based on the wrongCount.
        """
        self.t.ht()
        self.t.pensize(6)
        if (wrongCount == 1): # draw head
            self.t.circle(17)
        elif (wrongCount == 2): #draw body
            self.t.forward(60)
        elif (wrongCount == 3): #draw 1st arm
            self.t.back(45)
            self.t.right(30)
            self.t.forward(25)
        elif (wrongCount == 4): # draw 2nd arm
            self.t.back(25)
            self.t.left(60)
            self.t.forward(20)
        elif (wrongCount == 5): #draw 1st leg
            self.t.back(20)
            self.t.right(30)
            self.t.forward(45)
            self.t.right(15)
            self.t.forward(26)
        elif (wrongCount == 6): # draw 2nd leg
            self.t.back(26)
            self.t.left(30)
            self.t.forward(24)

            self.t.up()
            self.t.goto(0, -140)
            self.t.down()
            self.t.write("You lose!", font=("Arial", 15, "normal"))

    def graphicReset(self):
        """
        This function is to reset the drawing when player chooses to play again
        It is important because the Hangman object itself can not use turtle function directly
        """
        self.t.reset()
        
"""
a = Hangman()
a.start()
a.draw(1)
a.draw(2)
a.draw(3)
a.draw(4)
a.draw(5)
a.draw(6)
"""
