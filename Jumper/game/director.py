from game.display import Display
from game.comparison import Comparison
from game.word import Word

class Director:
    """ A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word (Word): Chooses the random word.
        comparison (Comparison): Compares the input word to the random word.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        display: For getting and displaying information, terminal service.
    """
    
    def __init__(self):
        """Constructs a new Director

        Args: 
            self (Director): an instance of Director.
        """
        self._word = Word()
        self.answers = []
        self._comparison = Comparison()
        self._is_playing = True
        self._display = Display()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._do_outputs()
            # shows display
            self._get_inputs()
            # Asks for inputs
            self.do_updates()
            # Makes sure game is still going
        
        self._do_outputs()
        # One final output of the guy dying or of victory

    def _do_outputs(self):
        """Provides the graphic
        
        Args:
            self (Director): An instance of Director.
        """
        self._display.display_jumper(self._word, self.answers, self._is_playing)
            # What will this need? Will it need both the word and comparison, and if so,
            # does that mean I should put it independently?
    
    def _get_inputs(self):
        """Gets user's input, validates it, and adds it to the list self.answers.
        Args:
        self (Director): An instance of Director.
        """
        user_input = input("Guess a letter [a-z]: ")
        possible_answers = [
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
            "p","q","r","s","t","u","v","w","x","y","z"
        ]
        while user_input.lower() != possible_answers:
            user_input = input("Oops!\nPlease guess a letter [a-z]: ")

        self.answers.append(user_input)
    
    def _get_updates(self):
        """Calls comparison to see if an input is part of the word

        Args:
            self (Director): An instance of Director.
        """
        self._comparison(self.answers, self._word)