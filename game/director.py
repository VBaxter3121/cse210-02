from game.cards import Cards

class Director:

    """
    """

    def __init__(self):

        self.score = 300
        self.currentGuess = ""
        self.isPlaying = True

    def start_game(self):
        """
        Begin the game setup and loop
        """
        
        print("""Welcome to HiLo! Every time a card is drawn, simply type 'higher' or 'lower' to
guess if the next card drawn will be higher or lower. Correct guesses will earn you
100 points, while incorrect guesses will loose you 75 points. If at any time you
have 0 points or less, the game will end. You can also type 'quit' to end the
game early.
""")
        cards = Cards()
        self.calculate(0)
        cards.draw()
        self.guess()

        while self.isPlaying:
            print()
            cards.draw()
            current = cards.current
            previous = cards.previous
            points = self.check_guess(current, previous)
            self.calculate(points)
            self.check_score()
            if self.isPlaying == True:
                self.guess()
        
        print(f"Game over! Your final score was {self.score}")

    def guess(self):
        """
        Prompt the player to guess if the next card will be higher or lower
        """
        guessValid = False
        while not guessValid:
            playerGuess = input("Higher or lower? ").lower()
            if playerGuess == "higher" or playerGuess == "lower":
                guessValid = True
                self.currentGuess = playerGuess
            elif playerGuess == "quit":
                self.isPlaying = False
                guessValid = True
            else:
                print("Invalid input!")

    def check_guess(self, current, previous):
        """
        Check if the players guess was correct or not
        """
        if (self.currentGuess == "higher" and current > previous)\
            or\
            (self.currentGuess == "lower" and current < previous):
            points = 100
        else:
            points = -75

        return points

    def calculate(self, points):
        """
        Add or subtract the appropriate amount of points and display the total
        """

        self.score += points
        print(f"Current score: {self.score}")

    def check_score(self):
        """
        Check if the player has enough points to keep playing
        """
        if self.score <= 0:
            self.isPlaying = False
