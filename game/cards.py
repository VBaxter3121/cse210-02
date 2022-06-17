import random

class Cards:

    def __init__(self):

        self.current = " "
        self.previous = ""

    def draw(self):
        """
        If this is the first card drawn:

        Choose a random number from 1-13, storing the value in self.current.
        If the number is the same as self.previous, try again until a different 
        number is produced.
        
        If another card has been drawn before:

        Move the value of self.current to self.previous before repeating the same
        process as before.
        """
        if self.current != " ":
            self.previous = self.current
        self.current = random.randint(1, 13)
        if self.current == self.previous:
            while self.current == self.previous:
                self.current = random.randint(1, 13)
        
        print(f"The card is {self.current}")