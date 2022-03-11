from game.card import Card

class Director:
    """A director, whose responsibility is to keep the 
    game going
    
    Attributes:
        firstcard (Card): The current card that will be asked upon.
        secondcard (Card): The next card that will be used to evaluate
        points (int): The score for the entire game.
        stay (boolean): Whether or not the game is being played.
        hilow (string): The current choice ('l' for lower, and 'h' for higher).
    """
    def __init__(self):
        """Constructor 
        Args: self (Director): an instance of Director
        """
        self.firstcard = None
        self.secondcard = None
        self.stay = True
        self.points = 300
        self.hilow = ""
        
    def start_game(self):
        """initialize the code
        Args: self (Director): 
        """        
        while self.stay:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()     
        
    def get_inputs(self):
        """Show firstcard and asks if the next card is higher or lower
        Args:
            self (Director): 
        """
    
        # If it's not the first game iteration, we 
        # should assign our last card to our self.firstcard here.
        if self.firstcard == None:
            self.firstcard = Card()
        else:
            self.firstcard = self.secondcard
    
        self.hilow = ""
        print(f"\nFIRT CARD: {self.firstcard.value}")
        while not self.hilow in ("l", "h"):
            self.hilow = input("THE SECOND CARD IS HIGHER OR LOWER? [h/l] ")
        
    def do_updates(self):
        """create the rules to compare the hi or low answer with the firstcard.
        Args:
            self (Director):
        """
        self.secondcard = Card()

        card = self.firstcard.value
        secondcard = self.secondcard.value

        if card < secondcard:
            if self.hilow == "h":
                self.points = self.points +100
            elif self.hilow == "l":
                self.points =self.points - 75
        elif card > secondcard:
            if self.hilow == "l":
                self.points =self.points + 100
            elif self.hilow == "h":
                self.points =self.points -75
        

    def do_outputs(self):
        """Displays the secondcard, the points and ask for keep play [y/n].
        Args:self (Director):
        """
        print("THE CAR WAS: % s"%self.secondcard.value)
        print("SCORE: % s"%self.points)

        keep_playing = ""
        while not keep_playing in ("y", "n"):
            keep_playing = input(f"STAY OR LEAVE [y/n]: ")

        if keep_playing == "n":
            self.stay = False
       
        